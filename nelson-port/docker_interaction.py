import docker

docker_client = docker.from_env()

def start_container(name):
    new_container = docker_client.containers.run('cca-interactive-run-redo', detach=True, stdin_open=True, stdout=True, tty=True, name=name, remove=True)
    print(new_container)
    print(type(new_container))
    print(dir(new_container))
    return(new_container.attach(stdout=True, stream=True, logs=True))

def get_stream(container_client):
    return(next(container_client._stream).decode())

def exec_user_cmd(cmd, container_client):
    container = docker_client.containers.get('cca_instance')
    return(container.exec_run(cmd, stream=True))


def attach_container(name):
    container = docker_client.containers.get(name)
    print(container)
    return(container.attach(stdout=True, stream=True, logs=True))