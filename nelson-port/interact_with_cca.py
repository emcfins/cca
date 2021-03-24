#!/usr/bin/env -S python3 -u

from time import sleep
import sys
import subprocess
from subprocess import Popen, PIPE
import select

global line
line = "."

def stdout_has_data(p):
    return select.select([p.stdout], [], [], 0.0)[0]


def stdin_has_data():
    return select.select([sys.stdin, ], [], [], 0.0)[0]


ON_POSIX = 'posix' in sys.builtin_module_names

binary_to_run = ["script", "--return", "--quiet", "-c", "/data/nelson-port/adventure.out"]

def print_waiting_stdout(p, line):
    print_out = []
    while stdout_has_data(p):
        line_from_app = p.stdout.readline()
        if line_from_app != '\n' and line_from_app != line:
            print(line_from_app)
            print_out.extend(line_from_app)
        # p.stdin.write("\n")
        p.stdout.flush()
        return(print_out)

def line_by_line_simple(p):
    print_in = []
    global line
    sleep(2)
    while True:
        print_out = print_waiting_stdout(p, line)
        if stdin_has_data():
            line = sys.stdin.readline()
            p.stdin.write(line)
            p.stdin.flush()
            print_in.append(print_in)
        sleep(0.5)



def main():
    p = Popen(binary_to_run, stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True, bufsize=1, close_fds=ON_POSIX)
    line_by_line_simple(p)

main()
