# Server handles messages and can send prompts back; it's similar to
50.
# Use threading for multiple clients.
import socket, threading
def handle(conn, addr):
 with conn:
    print('Connected', addr)
 while True:
    data = conn.recv(1024)
 if not data:
        break
 print('Client says:', data.decode())
 reply = input('Reply> ').encode()
 conn.sendall(reply)
s = socket.socket()
s.bind(('127.0.0.1', 9000))
s.listen()
while True:
 conn, addr = s.accept()
 threading.Thread(target=handle, args=(conn, addr),
daemon=True).start()