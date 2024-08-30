import os
import tkinter as tk
from tkinter import filedialog
import dropbox

# Dropbox access token
DROPBOX_ACCESS_TOKEN = 'sl-kWTmvw9q0GjX4sOHrRE2kTy6mcjP7G1ecFUFyvto'
# Authenticate with Dropbox API
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

# Get files in a specific folder with their sizes
def list_files_with_sizes(dbx, folder_path):
    try:
        files = dbx.files_list_folder(folder_path).entries
        if not files:
            print('No files found in the folder.')
        else:
            print('Files in the folder:')
            for file in files:
                print(f"{file.name} - Size: {file.size} bytes")
    except dropbox.exceptions.ApiError as e:
        if e.error.is_path() and e.error.get_path().is_not_found():
            print(f"Folder not found: {folder_path}")
        else:
            print(f"An API error occurred: {e}")

# Specify the Dropbox folder path where you want to list files
dropbox_folder_path_to_list = '/Photos'  # Use the correct path format
list_files_with_sizes(dbx, dropbox_folder_path_to_list)

# Create a file picker dialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
if not file_path:
    print("No file selected.")
else:
    file_name = os.path.basename(file_path)

    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read(), f"{dropbox_folder_path_to_list}/{file_name}")

    print("File uploaded.")

    root.mainloop()
