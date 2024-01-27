import requests
import os

def download_html(url, path):
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        os.remove(path)
        print("removed")

        # Write the HTML content to a file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"HTML downloaded successfully and saved as {path}")
    else:
        print("Failed to download HTML")

html_urls=[
    {"url":"https://www.salisbury.edu/admissions/transfer-students/academic-requirements.aspx", "path":"../data/html/Academic Requirements For Transfer Applicants | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/admissions-requirements.aspx","path":"../data/html/Admissions Requirements For Transfer Applicants | Salisbury University.html"}
    ]

for html_url in html_urls:
    download_html(html_url["url"],html_url["path"])
