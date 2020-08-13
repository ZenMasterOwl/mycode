#!/usr/bin/python3
def doesWork():
    a = input("Does the dang thing work?\n").lower().strip()
    if a == "yes": 
        return print("DON'T MESS WITH IT")
    elif a == "no":
        messedWith()
    else:
        doesWork()
def messedWith():
    a = input("Did you mess with it?\n").lower().strip()
    if a == "yes":
        print("You wormy scum")
        othersAlerted()
    elif a == "no":
        catchHeck()
    else:
        messedWith()
def othersAlerted():
    a = input("Does anyone know?\n").lower().strip()
    if a == "yes":
        poorBub()
    elif a == "no":
        print("Hide it")
        print("No problem")
    else:
        othersAlerted()
def catchHeck():
    a = input("Will you catch heck?\n").lower().strip()
    if a == "yes":
        poorBub()
    elif a == "no":
        print("Shoot - can it")
        print("No problem")
    else:
        catchHeck()
def poorBub():
    print("You poor bub...")
    a = input("Can you blame a private?\n").lower().strip()
    if a == "yes":
        print("No problem")
    else:
        poorBub()

doesWork()
