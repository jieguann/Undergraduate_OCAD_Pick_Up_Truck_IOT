import socket

s = socket.socket()
host = "127.0.0.1"
port = 9999
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('连接地址：', addr)
    data = c.recv(1024)
    print(data)
    c.send(b'iiiiii')
    c.close()