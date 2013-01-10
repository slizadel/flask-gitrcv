from flask import Flask, request, json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/rcv', methods=['POST'])
def rcv_hook():
    request_json = request.form.get('payload')
    app.logger.debug(request_json)
    app.logger.debug(type(request_json))
    request_json = json.loads(request_json)
    app.logger.debug(request_json['repository']['name'])

    return 'Payload'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
