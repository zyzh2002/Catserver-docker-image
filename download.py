import requests
import json

def getAddress():
    result = requests.get("https://api.github.com/repos/Luohuayu/Catserver/releases/latest").text
    data = json.loads(str(result))
    data = data['assets']
    data = data[0]
    data = data['browser_download_url']
    print(data)

def downloadFile(url):
    import wget
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    wget.download(url)
