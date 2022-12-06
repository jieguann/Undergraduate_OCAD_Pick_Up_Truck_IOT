from flask import Flask, render_template
from flask_socketio import SocketIO
import json as js
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

CarSpeed = None
HomeSound = None
def Bitcoin():
    bitcoin = js.loads(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").text)
    global CarSpeed
    jsonBitcoin = {'bitcoin': float(bitcoin['data']['amount'])}
    return jsonBitcoin


@socketio.on('CarSpeed')
def handle_my_custom_event(json):
    global CarSpeed
    CarSpeed = json
    print('received json: ' + str(json))

@socketio.on('HomeSound')
def handle_my_custom_event(json):
    global HomeSound
    HomeSound = json
    print('received json: ' + str(json))

@app.route('/')
def sessions():
    #For Car
    if CarSpeed == None:
        speed = 0
    else:
        SpeedData = CarSpeed.decode('utf-8')
        speed = js.loads(SpeedData)['CarSpeed']

    #For Home
    if HomeSound == None:
        sound = 0
    else:
        SoundData = HomeSound.decode('utf-8')
        sound = js.loads(SoundData)['HomeSound']


    CarJson = {'CarSpeed':speed}
    SoundJson= {'HomeSound': sound}
    json = {}
    json.update(Bitcoin())
    json.update(CarJson)
    json.update(SoundJson)
    return json


if __name__ == '__main__':
   socketio.run(app,debug=True)