import requests
import json

def getAddress():
    restlt = requests.get("https://api.github.com/repos/Luohuayu/Catserver/releases/latest").text
    