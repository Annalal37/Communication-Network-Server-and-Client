import socket
import threading

host = '127.0.0.1'
port = 9999
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(5)
saved = b''


def tcplink(conn, addr):
        global saved
        # print(conn, addr)
        request = conn.recv(1024)
        if request[0:3] == b'GET':
            # HTTP response message
            response = b'HTTP/1.1 200 OK\nContent-Type:text/html\r\n\r\n' \
                       b'<html><body><form method="post"><input name="name" value="' + saved + b'">' \
                       b'<button type="submit">Save</button></form></body></html>'
            conn.sendall(response)
        elif request[0:4] == b"POST":
            pos = request.find(b"\r\n\r\n")
            content = request[pos + 4:]
            response = b'HTTP/1.1 303 See Other\r\n' \
                       b'Location:/\r\n\r\n'
            saved = content[5:]  # b'name=
            conn.sendall(response)
            # print(content)
            # print(saved)
        conn.close()

def thread_func():
    global sock
    print("thread started")
    while 1:
        conn, addr = sock.accept()
        tcplink(conn, addr)

num_thread = 8
for i in range(num_thread):
    t = threading.Thread(target=thread_func)
    t.start()


