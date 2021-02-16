import requests
import json

def getAddress():
    result = requests.get("https://api.github.com/repos/Luohuayu/Catserver/releases/latest").text
    data = json.loads(str(result, encoding='utf-8'))
    data = data['assets']
    data = data['browser_download_url']
    print(data)