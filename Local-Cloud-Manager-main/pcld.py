import tkinter as tk
from tkinter import filedialog, messagebox
import requests

def upload_to_pcloud(file_path):
    # Your pCloud API details
    url = 'https://api.pcloud.com/uploadfile'
    folder_id = '18528042804'
    access_token = '3kDD7ZxcSoVXxAOuQZbpMQykZFNfBr4Vr3zB4206oBziB1hSJKrhy'

    files = {'file': (file_path.split('/')[-1], open(file_path, 'rb'))}

    params = {
        'access_token': access_token,
        'folderid': folder_id,
    }

    response = requests.post(url, files=files, params=params)
    return response

def open_file_dialog():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        global selected_files
        selected_files = list(file_paths)
        file_listbox.delete(0, tk.END)
        for file_path in selected_files:
            file_listbox.insert(tk.END, file_path)

def upload_selected_files():
    global selected_files
    if selected_files:
        uploaded_file_ids = []
        for file_path in selected_files:
            response = upload_to_pcloud(file_path)
            if response.status_code == 200:
                uploaded_file_ids.append(file_path)
                file_name = file_path.split('/')[-1]
                file_info.insert(tk.END, f"Uploaded: {file_name}\n")
        if uploaded_file_ids:
            messagebox.showinfo("Upload Complete", "Files uploaded successfully.")
        else:
            messagebox.showwarning("Upload Failed", "No files were uploaded.")
    else:
        messagebox.showwarning("No Files Selected", "Please select files before uploading.")

# Create the main window
root = tk.Tk()
root.title("pCloud File Uploader")

# Create GUI elements
select_button = tk.Button(root, text="Select Files", command=open_file_dialog)
upload_button = tk.Button(root, text="Upload Files", command=upload_selected_files)
file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50)
file_info = tk.Text(root, height=10, width=50)

# Arrange GUI elements
select_button.pack(pady=10)
file_listbox.pack()
upload_button.pack(pady=10)
file_info.pack()

# Initialize selected files list
selected_files = []

# Start the GUI event loop
root.mainloop()
