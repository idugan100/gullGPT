import requests
import sqlite3
try:
    url = input("Please enter the url: ")
    file_type = input("Please enter the file type (html, pdf): ")
    file_name = input("Please enter the file name: ")

    path = f"../data/{file_type}/{file_name}"

    response = requests.get(url)
        
    if response.status_code == 200:
        print("url works as expected")

        if file_type=="html":
            with open(path, 'w', encoding='utf-8') as f:
                f.write(response.text)
        elif file_type=="pdf":
            with open(path, 'wb') as pdf_file:
                pdf_file.write(response.content)
        else:
            print("unknown file type")
            exit(1)
        print(f"file downloaded successfully and saved to {path}")

        connection = sqlite3.connect("../data/data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO urls ('url','path','type') VALUES (?,?,?)",(url, path, file_type))
        connection.commit()
        connection.close()
        print("file information save to database")

    else:
        print("Failed to download file")
except Exception as e:
    print(e)