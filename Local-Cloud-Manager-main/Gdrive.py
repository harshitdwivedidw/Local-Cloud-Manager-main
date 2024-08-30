from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import tkinter as tk
from tkinter import filedialog

# Path to the downloaded client secret JSON file
CLIENT_SECRET_FILE = './client_secret_811176600692-2la9deha7bq0rk880mfj83kf6mki5i9d.apps.googleusercontent.com.json'

# Scopes define the access you need
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate and get credentials
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        # Write credentials to token.json
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

# Build the Drive API
service = build('drive', 'v3', credentials=creds)


# Get files in a specific folder with their sizes
def list_files_with_sizes(service, folder_id):
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query).execute()
    items = results.get('files', [])
    if not items:
        print('No files found in the folder.')
    else:
        print('Files in the folder:')
        for item in items:
            file_metadata = service.files().get(fileId=item['id'], fields='id,name,size').execute()
            size = file_metadata.get('size', 'Unknown')
            print(f"{item['name']} ({item['id']}) - Size: {size} bytes")

# Specify the folder ID where you want to list files
folder_id_to_list = '14C-o7nAtgF-Fy1PbqK6NqR9T_LkT5_Uh'
list_files_with_sizes(service, folder_id_to_list)



# Create a file picker dialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
if not file_path:
    print("No file selected.")
else:
    file_name = os.path.basename(file_path)
    media = MediaFileUpload(file_path)

    file_metadata = {
        'name': file_name,
        'parents': ['14C-o7nAtgF-Fy1PbqK6NqR9T_LkT5_Uh']
    }

    uploaded_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"File uploaded: {uploaded_file.get('id','name')}")


    root.mainloop()


# 
