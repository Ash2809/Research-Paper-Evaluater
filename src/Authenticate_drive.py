import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(r"C:\Users\aashutosh kumar\Downloads\Client_secrets.json")  # Update path 
    gauth.LocalWebserverAuth()  
    return gauth
