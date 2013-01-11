from flask import Flask, request, json
from git import *
app = Flask(__name__)

REPO = '/opt/flask-gitrcv'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/rcv', methods=['POST'])
def rcv_hook():
    # Grab the JSON from the POST request
    request_json = request.form.get('payload')
    request_json = json.loads(request_json)
    app.logger.debug(request_json['repository']['name'])

    # Setup the git repo. 
    repo = Repo(REPO)
    origin = repo.remotes.origin

    # Pull in the latest version.
    origin.pull()

    return 'Payload'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
