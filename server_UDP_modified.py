import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
def udplink(data, addr):
    print('Received from %s:%s.' % addr)
    s.sendto(b'%s' % data, addr)


def thread_func():
    global s
    print("thread started")
    while 1:
        conn, addr = s.recvfrom(1024)
        udplink(conn, addr)

num_thread = 8
for i in range(num_thread):
    t = threading.Thread(target=thread_func)
    t.start()
