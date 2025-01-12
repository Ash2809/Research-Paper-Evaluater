import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def fetch_pdfs_from_drive(auth, folder_id, download_dir):
    drive = GoogleDrive(auth)  
    query = f"'{folder_id}' in parents and mimeType='application/pdf'"
    file_list = drive.ListFile({'q': query}).GetList()

    print(f"Found {len(file_list)} PDF files in the folder.")
    for file in file_list:
        print(f"Downloading {file['title']}...")
        file.GetContentFile(f"{download_dir}/{file['title']}")
    print("All files downloaded successfully!")