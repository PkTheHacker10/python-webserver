try:
    from modules import os
except ImportError as Ie:
    print(f"Import Error on [File_Handler]: {Ie}")
    exit(1) 
     
class FileHandlerClass:
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
     