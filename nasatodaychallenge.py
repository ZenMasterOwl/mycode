#!/usr/bin/python3
import requests
import wget
querylist = []
date = input("Welcome to nasa's apod api, please enter a day in the format YYYY-MM-DD:\n") or "1996-04-16"

baseurl = "https://api.nasa.gov/planetary/apod?"
hd = input("Would you like your picture to download in high definition? Enter 'y' or 'n':\n")
if date != "":
    date = "date=" + date
    querylist.append(date)
if hd != "":
    if hd == "y":
        hd = "hd=true"
    else:
        hd = "hd=false"
    querylist.append(hd)
querylist.append(apikey)

queryparams = "&".join(querylist)
url = baseurl + queryparams
res = requests.get(url)
json_data = res.json()
print(json_data["title"])
print(json_data["date"])
print(json_data["explanation"])
wget.download(json_data["url"], '/home/student/mycode/nasapic')

