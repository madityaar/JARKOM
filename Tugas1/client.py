# encoding=utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="127.0.0.1"
port =8002
s.connect((host,port))

def ts(str):
   x = input("enter message plz: ")
   s.send(x.encode())
   data = ''
   data = s.recv(1024).decode()
   print (data)

while 2:
   ts(s)

s.close ()
exit()
