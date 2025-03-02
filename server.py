#!/bin/python3
import socket

class file_handler:
    def get_file_content(self, file):
        pass

class socket_handler:
    def __init__(self):
        self.host=''
        self.port=8080
    def create_socket(self):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock

class http_handler:
    def request(self):
        pass

class webserver:
    def __init__(self):
        self.file_handler = file_handler()
        self.http_handler = http_handler()
        self.socket_handler = socket_handler()
    def webserver_handler(self):
        sock=self.socket_handler.create_socket()
        sock.listen()
        print('Server started on port %s' % self.socket_handler.port)
        conn, addr = sock.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        print('Received', repr(data))


def main():
    server = webserver()
    server.webserver_handler()  

if __name__ == '__main__':
    main()