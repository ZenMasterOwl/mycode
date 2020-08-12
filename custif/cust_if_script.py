#!/usr/bin/python3

result = 0

def func(answer):
    global result
    if answer == 0:
        result += 1
    elif answer == 1:
        result += 2
    else: 
        result += 3

def findElement(result):
    if result < 3:
        return "Fire"
    elif result < 5:
        return "Water"
    else:
        return "Air"
answer = int(input("\nHow do you handle rejection?\n0: Rage | 1: I Freeze | 2: I just move on  "))
func(answer)
answer = int(input("\nWhat makes you feel at home?:\n0: Volcano | 1: Ocean | 2: Skyscapes "))
func(answer)

print(f"\nYour element is {findElement(result)}")
