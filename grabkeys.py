# getkeys.py
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

#function used in the Sentdex videos, grabs the keys used when run, allows input to be transformed into something that can be passed into the neural net
import win32api as wapi
import time
from pynput import mouse

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys




