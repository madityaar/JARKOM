# encoding=utf-8

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8002
data = ""
print (host)
print (port)
serversocket.bind(("127.0.0.1", 8002))

serversocket.listen(5)
print ('server started and listening')
while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!")
    while data != "exit":
        data = clientsocket.recv(5120).decode("utf-8")
        print ("string from client: ",data)
        if data != "exit":
            r="Receieved!"
        else:
            r="server closing"
        clientsocket.send(r.encode())

exit()
