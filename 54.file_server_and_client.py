# Server
import socket
s = socket.socket()
s.bind(('0.0.0.0', 6000))
s.listen(1)
conn, addr = s.accept()
with conn, open('sendfile.bin','rb') as f:
 for chunk in iter(lambda: f.read(4096), b''):
    conn.sendall(chunk)
# Client
import socket
s = socket.socket()
s.connect(('127.0.0.1', 6000))
with open('received.bin','wb') as f:
 while True:
    data = s.recv(4096)
 if not data: 
    break
 f.write(data)