#!/usr/bin/python3
import os
import socket
    
class file_handler:
    def __init__(self):
        self.root_dir='src'
        self.available_docs=[]
        
    def get_available_docs(self):
        files=os.listdir(self.root_dir)
        for html_file in files:
            if html_file.endswith(".html"):
                self.available_docs.append(html_file)
        return self.available_docs
    
    def get_file_content(self, file):
        with open("src/"+file, 'r') as f:
            return f.read()
        
class socket_handler:
    def __init__(self):
        self.host='192.168.33.97'
        self.port=8080
        
    def create_socket(self):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        return sock

class http_handler:
    def __init__(self):
        self.file_handler = file_handler()
        
    def get_requested_file(self, data):
        requested_file = data.split('\n')[0].split(' ')[1]
        return requested_file
    
    def get_request_method(self,data):
        return data.split('\n')[0].split(' ')[0]
    
    def get_connected_host(self, data):
        return data.split('\n')[1].split(' ')[1]
    
    def http_handler(self,requested_data):
        # http_handler Function
        requested_doc=self.get_requested_file(requested_data)
        if requested_doc == '/':
            requested_doc ='index.html'
            
        requested_doc=requested_doc.split('/')[1]
        
        if requested_doc.startswith('src'):
            requested_doc='404.html'
            
        if requested_doc == '/favicon.ico':
            pass
        
        if requested_doc in self.file_handler.get_available_docs():
            requested_doc_contents=self.file_handler.get_file_content(requested_doc)
            return requested_doc_contents
        else:
            requested_doc_contents=self.file_handler.get_file_content('404.html')
            return requested_doc_contents

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
                request_data=conn.recv(2048).decode()
                requested_file=self.http_handler.get_requested_file(request_data)
                requested_method=self.http_handler.get_request_method(request_data)
                requested_host=self.http_handler.get_connected_host(request_data)       
                if requested_file != 'favicon.ico':
                    print(f"Connected host: {requested_host} Requested file: {requested_file} Requested method :{requested_method}")
                    requested_doc=self.http_handler.http_handler(request_data)
                    conn.sendall(requested_doc.encode())
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