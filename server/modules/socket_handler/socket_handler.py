try:
    from modules import socket
except ImportError as Ie:
    print(f"Import Error on [Socket_Handler]: {Ie}")
    exit(1)  
    
class SocketHandlerClass:  
    # Class to handle socket.
    def create_socket(self):
        # Function to create a socket channel.
        HOST='192.168.33.97'
        PORT=8080
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST,PORT))
        print('Server started @ port : %s' % PORT)
        return sock

