# cca

Let's make [America Colossal Cave Adventure] (https://en.wikipedia.org/wiki/Colossal_Cave_Adventure) again!

Based upon Fortran code found on [Jerz's Literacy Weblog] (http://jerz.setonhill.edu/intfic/colossal-cave-adventure-source-code/)

### To Compile as of October 28, 2016

```
gfortran -g -Wall -Wextra -Warray-temporaries -Wconversion -fimplicit-none -fbacktrace -ffree-line-length-0 -fcheck=all -ffpe-trap=zero,overflow,underflow -finit-real=nan advf4-77-03-31.f 
```

## Using the Dockerfile

When in the same directory as the README.md, run:
```
docker build -t cca .

docker run -it -v <location of project>:/data cca
```

### Things I've learned so far by Erin

* vim is awesome becuase it does syntax highlighting for Fortran. SUPER helpful

* when talking about this project, I say 4chan instead of Fortran 9 times out of 10

* all commands have to start at column 7

* to convert the tabs to 6 spaces

```
:set tabstop=4 shiftwidth=4 expandtab
:%!expand -t6
```
