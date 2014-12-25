'''
@author: rkzhang
'''
import socket_sample

HOST = ''
PORT = 50011

sock = socket_sample.socket_sample(socket_sample.AF_INET, socket_sample.SOCK_STREAM)
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