from src.Authenticate_drive import authenticate_drive
from src.Pdf_fetcher import fetch_pdfs_from_drive
from src.process import process_papers_from_drive
import os

folder_id = "1Y2Y0EsMalo26KcJiPYcAXh6UzgMNjh4u"  
download_dir = r"C:\Projects\Research-Paper-Evaluater\data"
output_csv = "results.csv"  

os.makedirs(download_dir, exist_ok=True)

drive = authenticate_drive()
fetch_pdfs_from_drive(drive, folder_id, download_dir)

process_papers_from_drive(download_dir, output_csv)