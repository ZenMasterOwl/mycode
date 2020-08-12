#!/usr/bin/python3

string = ""
x=0
y=10
while x < 9:
    x += 1
    y -= 1
    if x < 6:
        string += "* "
        print(string)
    else:
        print(string[0:(y*2)])



"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""