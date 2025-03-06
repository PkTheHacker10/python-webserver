try:
    from modules import file_handler
    from modules import http_handler
    from modules import socket_handler
    
except ImportError as Ie:
    print(f"Import Error on [Main_Handler]: {Ie}")    
    exit(1) 
    
class webserver:
    def __init__(self):
        # Gathering all classes from modules.
        self.socket_handler=socket_handler()()
        self.http_handler=http_handler()()
        self.file_handler=file_handler()()
        
    def webserver_handler(self):
        # Web server handler funtion to handle the web server.
        sock=self.socket_handler.create_socket()
        sock.listen()
        while True:
            try:
                conn, addr = sock.accept()
                request_data=conn.recv(2048).decode()
                requested_doc=self.http_handler.http_handler(request_data)
                requested_file=self.http_handler.get_requested_file(request_data)
                requested_method=self.http_handler.get_request_method(request_data)
                requested_host=self.http_handler.get_connected_host(request_data)       
                print(f"Connected host: {requested_host.split(":")[0]} Requested file: {requested_file} Requested method :{requested_method}")
                conn.sendall(requested_doc.encode())
                conn.close()
                
            except KeyboardInterrupt:
                print('\nServer shutting down...')
                sock.close()
                break
            except Exception as Ue:
                print(f"Unexpected Error Occoured :{Ue}")

def main():
    # Main funtion to start the server.
    server = webserver()
    server.webserver_handler()  
    
if __name__=="__main__":
    main()
        