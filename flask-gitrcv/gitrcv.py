from flask import Flask, request, json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/rcv', methods=['POST'])
def rcv_hook():
    app.logger.debug(request.data)
    if request.headers['Content-Type'] == 'application/json':
        print json.dumps(request.json)
        return json.dumps(request.json)
    else:
        return request.headers['Content-Type']

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
