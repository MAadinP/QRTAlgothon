from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
import os
import time
import io

# Service account key file (replace with your path)
SERVICE_ACCOUNT_FILE = 'PATH'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Folder ID of the shared Google Drive folder
FOLDER_ID = '1ElVOO_4Plr24xEOmdqsINmIRM_y4M3_n'

# Local directory to save the downloaded files
DOWNLOAD_DIR = 'data_download/'

# Authenticate and build the service
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def get_latest_file():
    """Fetch the latest file from the shared folder."""
    query = f"'{FOLDER_ID}' in parents and trashed = false"
    results = service.files().list(
        q=query,
        orderBy='createdTime desc',  # Order by newest
        fields="files(id, name, createdTime)"
    ).execute()
    files = results.get('files', [])
    if files:
        return files[0]  # Return the latest file
    return None

def download_file(file_id, file_name):
    """Download a file by its ID."""
    request = service.files().get_media(fileId=file_id)
    file_path = os.path.join(DOWNLOAD_DIR, file_name)

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)  # Ensure the download directory exists
    with io.FileIO(file_path, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")
    print(f"File downloaded: {file_path}")

def monitor_and_download():
    """Monitor the folder and download new files."""
    seen_files = set()
    
    while True:
        latest_file = get_latest_file()
        if latest_file:
            file_id = latest_file['id']
            file_name = latest_file['name']
            if file_id not in seen_files:
                print(f"New file detected: {file_name}")
                download_file(file_id, file_name)
                seen_files.add(file_id)
            else:
                print("No new files.")
        else:
            print("No files found in the folder.")
        time.sleep(19 * 60)  # Wait for 19 minutes

# Start monitoring
monitor_and_download()
