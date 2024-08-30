import tkinter as tk
from tkinter import filedialog
from boxsdk import OAuth2, Client
import boxsdk

# Set your Box application credentials
CLIENT_ID = 'ws64vbjjvnkw76roo45133nsvcizkxx0'
CLIENT_SECRET = 'mk2JjlWHVHB634nrIq4jBH2x15zLL0dk'

# Set your existing access token and refresh token
EXISTING_ACCESS_TOKEN = '3yPnHEvpfthB8cBSE73RWdA5z6UwI2Co'
EXISTING_REFRESH_TOKEN = 'GOATAd1Ek3P7tdlKTND55c4BOexyMozakbLAldI3iMHPySMPV7xpd74iEaBaGv7f'

# Set up OAuth2 flow with existing tokens
oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=EXISTING_ACCESS_TOKEN, refresh_token=EXISTING_REFRESH_TOKEN)

# Create the client
client = Client(oauth2)

# Tkinter GUI
class BoxUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Box.com File Uploader")

        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=20)
        
        self.list_files_button = tk.Button(root, text="List Files", command=self.list_files)
        self.list_files_button.pack()

        self.folder_id = '223342707885'  # Change this to the appropriate folder ID


    def list_files(self):
        folder = client.folder(self.folder_id).get()
        items = folder.get_items()
        
        print("Files in the folder:")
        for item in items:
            if isinstance(item, boxsdk.object.file.File):
                file_info = client.file(item.id).get()
                print(f"File: {item.name}, size {file_info.size} bytes")
                 

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = file_path.split("/")[-1]
            folder = client.folder(self.folder_id).get()
            uploaded_file = folder.upload(file_path, file_name)
            uploaded_size = uploaded_file.size
            print(f"File '{uploaded_file.name}' with size: '{uploaded_size}' bytes")
    


# Create the main window
root = tk.Tk()
app = BoxUploaderApp(root)
root.mainloop()
