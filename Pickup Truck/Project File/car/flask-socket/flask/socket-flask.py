from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

dataJson = None

@socketio.on('my event')
def handle_my_custom_event(json):
    global dataJson
    dataJson = json
    print('received json: ' + str(json))

@app.route('/')
def sessions():
    bitcoin = json.loads(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").text)
    global dataJson
    jsonBitcoin = {'bitcoin': float(bitcoin['data']['amount'])}

    if dataJson == None:
        jsonBitcoin.update({'CarSpeed': 0})

        return jsonBitcoin
    else:
        Data = dataJson.decode('utf-8')
        JsonData = json.loads(Data)
        jsonBitcoin.update(JsonData)
        return jsonBitcoin


if __name__ == '__main__':
   socketio.run(app, debug=True, host='127.0.0.1')