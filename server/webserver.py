try:
    from modules import file_handler
    from modules import http_handler
    from modules import socket_handler
    
except ImportError as Ie:
    print(f"Import Error on [Main_Handler]: {Ie}")    
    exit(1) 
    
class webserver:
    def __init__(self):
        # Gathering all classes from package.
        self.socket_handler_class=socket_handler()
        self.http_handler_class=http_handler()
        self.file_handler_class=file_handler()
        
    def webserver_handler(self):
        # Initializing all classes.
        _socket_handler=self.socket_handler_class()
        _http_handler=self.http_handler_class()
        _file_handler=self.file_handler_class()
        sock=_socket_handler.create_socket()
        sock.listen()
        while True:
            try:
                conn, addr = sock.accept()
                request_data=conn.recv(2048).decode()
                requested_doc=_http_handler.http_handler(request_data)
                requested_file=_http_handler.get_requested_file(request_data)
                requested_method=_http_handler.get_request_method(request_data)
                requested_host=_http_handler.get_connected_host(request_data)       
                if requested_file != 'favicon.ico':
                    print(f"Connected host: {requested_host.split(":")[0]} Requested file: {requested_file} Requested method :{requested_method}")
                    conn.sendall(requested_doc.encode())
                conn.close()
                
            except KeyboardInterrupt:
                print('\nServer shutting down...')
                sock.close()
                break

def main():
    server = webserver()
    server.webserver_handler()  
    
if __name__=="__main__":
    main()
        