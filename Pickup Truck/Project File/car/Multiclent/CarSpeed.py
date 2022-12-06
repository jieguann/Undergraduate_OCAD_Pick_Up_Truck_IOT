import json
import socketio
import time

sio = socketio.Client()


def send_ping():
    while True:

        
        send()
        time.sleep(.1)






def send():
    jsonData = {'test': 5}
    #jsonData = {'CarSpeed': capture()}
    Data = json.dumps(jsonData).encode('utf-8')
    #print(type(Data))
    #print(Data)
    sio.emit('test', Data)
    #print('my sid is', sio.sid)







@sio.event

def connect():


    print('connected to server')

    send_ping()

if __name__ == '__main__':

    #sio.connect('http://localhost:5000')
    sio.connect('http://52.168.69.101:1234')
