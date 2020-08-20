import threading
import os

def canthisdostuff():
    print("do this stuff")

something = threading.Thread(target=canthisdostuff())
something.start()
