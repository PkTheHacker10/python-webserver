# Importing Built-in modules  

import os
import socket

# Importing Custom modules by lazy loading

def file_handler():
    from modules.file_handler.file_handler import FileHandlerClass 
    return FileHandlerClass

def socket_handler():
    from modules.socket_handler.socket_handler import SocketHandlerClass
    return SocketHandlerClass

def http_handler():
    from modules.http_handler.http_handler import HttpHandlerClass
    return HttpHandlerClass

__all__=["os","socket"]