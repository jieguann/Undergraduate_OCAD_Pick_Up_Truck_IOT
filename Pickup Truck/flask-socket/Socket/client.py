import socket
import json
# Create a socket object

port = 12345
s = socket.socket()
s.connect(('127.0.0.1', port))

while 1:
   data = {'sod': 15.99}
   dataJson = json.dumps(data).encode('utf-8')
   s.sendall(dataJson)
   data = s.recv(1024)
   print(data)


