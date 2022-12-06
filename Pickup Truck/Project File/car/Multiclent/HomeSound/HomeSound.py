import json
import socketio


sio = socketio.Client()

def send_ping():
    while True:
        data = 'jie'
        
        sio.emit('test', data)
        #print('my sid is', sio.sid)
    # data = s.sound()
    # jsonData = {'HomeSound': data}
    # Data = json.dumps(jsonData).encode('utf-8')
    # print(type(Data))
    # sio.emit('HomeSound', Data)
    # print('my sid is', sio.sid)


@sio.event

def connect():

    print('connected to server')

    send_ping()

if __name__ == '__main__':

    sio.connect('http://localhost:5000')
    #sio.connect('http://165.22.237.47:5000')
