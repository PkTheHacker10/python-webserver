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
        # Funtion to get all the files from the root dir.
        # TODO: it only extracting .html files need to get all the sub dirs from the root dir. 
        files=os.listdir(self.root_dir)
        for html_file in files:
            if html_file.endswith(".html") or html_file.endswith(".jpg") or html_file.endswith(".css") or html_file.endswith(".php"):
                self.available_docs.append(html_file)
        return self.available_docs
    
    def get_file_content(self, file):
        file_path=os.path.join(self.root_dir,file)
        with open(file_path, 'rb') as opened_file:
            content=opened_file.read()
            try:
                return content.decode("utf-8") 
            except UnicodeDecodeError:
                return content 
            except Exception as ue:
                print(f"Unexpected error [FileHandler] :{ue}")

     