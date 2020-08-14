#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import wget
def main():
    input_pokemon = input("Please enter the name of the Pokemon you'd like to look up: ")
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{input_pokemon}")
    temp = r.json().get("all")
    url = "https://www.python.org/static/img/python-logo@2x.png"
    wget.download(url,'/home/student/mycode/image.png')
main()

