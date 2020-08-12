#!/usr/bin/python3

def func(answer):
    if answer == "0":
        print("0")
    elif answer =="1":
        print("1")
    else: 
        print("2")

answer = input("Please type a number between 0 and 2 ")
func(answer)
