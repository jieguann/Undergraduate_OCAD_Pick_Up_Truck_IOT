import socket
import json
# Create a socket object

port = 12345
s = socket.socket()
s.connect(('127.0.0.1', port))
while 1:
   data = s.recv(1024).decode('utf-8')
   # jsonData = json.dumps(data)
   # jsonLoad = json.loads(jsonData)
   # json = json.loads(jsonData)
   # print(data['sound'])
   # jsonData = json.loads(data.decode('utf-8'))
   # jsonData = json.loads(data)
   print(data)
   # print(jsonLoad)
   print(type(data))
   # print(json)
   # print(jsonData["sod"])