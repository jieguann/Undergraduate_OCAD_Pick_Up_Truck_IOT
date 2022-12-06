import socket

# next create a socket object
s = socket.socket()

port = 12345

s.bind(('', port))


# put the socket into listening mode
s.listen(5)

# Establish connection with client.
c, addr = s.accept()
print('One connect')
c1, addr = s.accept()

# a forever loop until we interrupt it or
# an error occurs
while True:
    data = c.recv(1024)
    # send a thank you message to the client.
    c1.sendall(data)
    c.sendall(data)
    # Close the connection with the client
