try:
    from modules import file_handler
except ImportError as Ie:
    print(f"Import Error on [Http_handler]: {Ie}")
    exit(1) 
    
class HttpHandlerClass:
    # Class to handle http request and response.
    # TODO : need to make a template for response before send back to the requested client.
    def __init__(self):
        self.file_handler=file_handler()     
           
    def get_requested_file(self,requested_data):
        # Funtion to extract requested file from the client request
        return requested_data.split('\n')[0].split(' ')[1]
    
    def get_request_method(self,requested_data):
        # Funtion to extract requested method from the client request
        return requested_data.split('\n')[0].split(' ')[0]
    
    def get_connected_host(self,requested_data):
        # Funtion to extract requested host from the client request
        return requested_data.split('\n')[1].split(' ')[1]
    
    def http_handler(self,requested_data):
        # http_handler Function
        _file_handler=self.file_handler()
        requested_doc=self.get_requested_file(requested_data)
        if requested_doc == '/':
            requested_doc ='index.html'
            
        requested_doc=requested_doc.split('/')[1]
        
        if requested_doc.startswith('src'):
            requested_doc='404.html'
            
        if requested_doc == '/favicon.ico':
            pass
        
        if requested_doc in _file_handler.get_available_docs():
            requested_doc_contents=_file_handler.get_file_content(requested_doc)
            return requested_doc_contents
        else:
            requested_doc_contents=_file_handler.get_file_content('404.html')
            return requested_doc_contents
