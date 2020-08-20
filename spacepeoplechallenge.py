#!/usr/bin/python3
import requests
url = "http://api.open-notify.org/astros.json"
res = requests.get(url)
data = res.json()
print("People in space")
for person in data["people"]:
    print(f"{person['name']} on the {person['craft']}")
