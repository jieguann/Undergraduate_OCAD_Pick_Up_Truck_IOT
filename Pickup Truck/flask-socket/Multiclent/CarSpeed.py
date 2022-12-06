import json
import socketio
import obd
import socketio
sio = socketio.Client()


def send_ping():
    while True:


        send()






def send():
    jsonData = {'CarSpeed': 5}
    #jsonData = {'CarSpeed': capture()}
    Data = json.dumps(jsonData).encode('utf-8')
    print(type(Data))
    print(Data)
    sio.emit('CarSpeed', Data)
    print('my sid is', sio.sid)



def capture():
    connection = obd.OBD()  # auto-connects to USB or RF port

    cmd = obd.commands.SPEED  # select an OBD command (sensor)

    response = connection.query(cmd)  # send the command, and parse the response

    print(response.value)  # returns unit-bearing values thanks to Pint

    return response.value





@sio.event

def connect():


    print('connected to server')

    send_ping()

if __name__ == '__main__':

    #sio.connect('http://localhost:5000')
    sio.connect('http://165.22.237.47:5000')