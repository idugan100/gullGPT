import requests
import os
import sqlite3
from datetime import datetime
startTime = datetime.now()

def download_new_file(url, path, type):
    response = requests.get(url)
    
    if response.status_code == 200:
        os.remove(path)
        print("removed old file")

        if type=="html":
            with open(path, 'w', encoding='utf-8') as f:
                f.write(response.text)
        elif type=="pdf":
            with open(path, 'wb') as pdf_file:
                pdf_file.write(response.content)
        else:
            print("unknown file type - skipping")
            return
        print(f"file downloaded successfully and saved as {path}")
    else:
        print("Failed to download file")

connection = sqlite3.connect("../data/data.db")
cursor = connection.cursor()
for url in cursor.execute("SELECT * FROM urls"):
    download_new_file(url[1],url[2],url[3])

connection.close()

print(datetime.now() - startTime)
