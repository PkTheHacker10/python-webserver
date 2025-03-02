#!/bin/python3
import socket

class file_handler:
    def get_file_content(self, file):
        with open("src/"+file, 'r') as f:
            return f.read()
class socket_handler:
    def __init__(self):
        self.host='172.30.16.116'
        self.port=8080
    def create_socket(self):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock

class http_handler:
    def __init__(self):
        self.file_handler = file_handler()
        
    def get_requested_file(self, data):
        requested_file = data.split('\n')[0].split(' ')[1]
        if requested_file == '/':
            return 'index.html'
        if requested_file.startswith('src'):
            pass
        if requested_file == 'favicon.ico':
            pass
        return requested_file[1:] 
    
    def get_request_method(self,data):
        return data.split('\n')[0].split(' ')[0]
    
    def get_connected_host(self, data):
        return data.split('\n')[1].split(' ')[1]
    
    def response(self,file):
        return self.file_handler.get_file_content(file)

class webserver:
    def __init__(self):
        self.file_handler = file_handler()
        self.http_handler = http_handler()
        self.socket_handler = socket_handler()
        
    def webserver_handler(self):
        sock=self.socket_handler.create_socket()
        sock.listen()
        print('Server started on port %s' % self.socket_handler.port)
        while True:
            try:
                conn, addr = sock.accept()
                # conn.sendall(self.http_handler.response('index.html').encode())
                data=conn.recv(2048).decode()
                
                
                requested_file=self.http_handler.get_requested_file(data)
                requested_method=self.http_handler.get_request_method(data)
                requested_host=self.http_handler.get_connected_host(data)
                
                
                if requested_file != 'favicon.ico':
                    print(f"Connected host: {requested_host} Requested file: {requested_file} Requested method :{requested_method}")
                    conn.sendall(self.http_handler.response(requested_file).encode())
                conn.close()
            except KeyboardInterrupt:
                print('\nServer shutting down...')
                sock.close()
                break

def main():
    server = webserver()
    server.webserver_handler()  

if __name__ == '__main__':
    main()