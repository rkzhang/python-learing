'''
@author: rkzhang
'''
import socket

HOST = ''
PORT = 50011

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

conn, address = sock.accept()

print 'ConnectedBy', address

while True :
    data = conn.recv(1024)
    if not data : 
        break
    conn.sendAll(data)
    
conn.close