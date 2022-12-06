from flask import Flask, render_template
from flask_socketio import SocketIO
import json as js




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#CarSpeed = None
test = None

@socketio.on('test')
def handle_my_custom_event(json):
    global test
    test = json
    print('received json: ' + json)

@app.route('/')
def sessions():
    if test == None:
        _test = 0
    else:
       #__test = test.decode('utf-8')
       #_test = js.loads(__test)['test']
       _test = test
       
        


    #CarJson = {'CarSpeed':speed}
    testJson= {'HomeSound': _test}
    print(_test)
    json = {}
    
    #json.update(CarJson)
    json.update(testJson)
    return json


if __name__ == '__main__':
   socketio.run(app,host='0.0.0.0',debug=True)
