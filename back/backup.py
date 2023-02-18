import pyautogui as pgui
import keyboard
from time import sleep


for i in range(1):
    if keyboard.read_key() == "n":
        pgui.click(775, 830)
    elif keyboard.read_key() == "m":
        pgui.click(1415, 830)
    elif keyboard.read_key()== "k":
        nextxy = pgui.locateOnScreen("img/next.png", confidence=0.9)
        pgui.click(nextxy)
        sleep(.5)
        okxy = pgui.locateOnScreen("img/ok.png", confidence=0.9)
        pgui.click(okxy)
    elif keyboard.read_key() == "l":
        goalxy = pgui.locateOnScreen("img/goal.png", confidence=0.9)
        pgui.click(goalxy)
        sleep(.5)
        okxy = pgui.locateOnScreen("img/ok.png", confidence=0.9)
        pgui.click(okxy)
        sleep(.3)
        yesxy = pgui.locateOnScreen("img/yes.png", confidence=0.9)
        pgui.click(yesxy)
    elif keyboard.read_key() == "j":
        inputxy = pgui.locateOnScreen("img/tex_input.png", confidence=0.5)
        x,y = pgui.center(inputxy)
        pgui.click(x,y+60) 
        for i in range(40):
            pgui.typewrite('.\n')
            pgui.press('enter')
        goalxy = pgui.locateOnScreen("img/goal.png", confidence=0.9)
        pgui.click(goalxy)
        sleep(.5)
        okxy = pgui.locateOnScreen("img/ok.png", confidence=0.9)
        pgui.click(okxy)