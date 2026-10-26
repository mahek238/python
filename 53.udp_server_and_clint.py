# UDP Server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
while True:
 data, addr = s.recvfrom(1024)
 print('Received', data, 'from', addr)
 s.sendto(b'ACK', addr)
# UDP Client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Hello UDP', ('127.0.0.1', 9999))
data, addr = s.recvfrom(1024)
print('Response', data)
