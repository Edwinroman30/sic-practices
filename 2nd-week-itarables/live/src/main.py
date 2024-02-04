import requests
import json

resp = requests.get("https://api.itbook.store/1.0/search/docker")

data = resp.json()

for d in data["books"]:
    print(d["title"])