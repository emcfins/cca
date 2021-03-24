from flask import Flask, render_template, request, redirect, url_for
import docker_interaction

app = Flask(__name__)
global new_container

@app.route('/', methods=['GET', 'POST'])
def user_action_form():
    global new_container
    # present the form
    title = 'Colosal Cave Adventure'
    subtitle = 'Colosal Cave Adventure - Special Projects Edition!'
    container_name = 'cca_instance'
    base_url = 'index.html'
    entries = []
    game_response = ''
    print(request.method)
    if request.method == 'GET':
        return render_template(base_url, title=title, subtitle=subtitle)
    # How will we connect to the container - perhaps we should start the container before the game?
    # I'd like to spin a container up every time we do a start - then keep the connection consistent, 
    # or at least somehow connect every time - how to consist with the container info
    if request.method == 'POST':
        entries = list(request.form.items())[0]
        print(entries)
        if entries[1] == 'start':
            # TODO: if there is a running container, do a popup and check if they want to start over, 
            # if do, delete and recreate container
            # if not, just attach without starting up a new one
            new_container = docker_interaction.start_container(container_name)
            print(new_container)
            print(dir(new_container))
            print(type(new_container))
            container_attach = docker_interaction.attach_container(container_name)
            print(container_attach)
            game_response = docker_interaction.get_stream(container_attach)
            print(game_response)
            # return redirect(url_for('user_action_form'))
            # return render_template('index.html', title=title, subtitle=subtitle, user_action=entries[1])
        else:
            container_attach = docker_interaction.attach_container(container_name)
            container_response = docker_interaction.exec_user_cmd(entries[1], container_attach)
            print(container_response)
            game_response = docker_interaction.get_stream(container_response)
            print(game_response)
            
        # interact_with_cca(entries[1])
    return render_template('index.html', title=title, subtitle=subtitle, game_response=game_response, user_action=entries[1])

if __name__ == "__main__":
    app.run(debug=True)
