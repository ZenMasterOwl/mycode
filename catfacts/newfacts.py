#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    temp = r.json().get("all")
    newlist = []
    for each in temp:
         newlist.append(each.get("upvotes"))
    sortedlist = newlist.sort()
    print(f"The most upvoted cat fact received {sortedlist[-1]} votes!!!\nCongratulations!")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    #print(r.json().get("all").get("user").get("name").get("first"))
main()

