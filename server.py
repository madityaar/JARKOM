import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8000
data = ""
print (host)
print (port)
serversocket.bind(("127.0.0.1", 8000))

serversocket.listen(5)
print ('server started and listening')
while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!")
    while data!="exit":
        data = clientsocket.recv(1024).decode("utf-8")
        print ("string from client: ",data)
        if data!="exit"
            r="Receieved!"
        else
            r="server closing"
        clientsocket.send(r.encode())
