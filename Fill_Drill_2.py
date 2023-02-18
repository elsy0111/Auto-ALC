import pyautogui as pgui
from time import sleep

pgui.press("F12")
sleep(.5)
pgui.hotkey('ctrl', 'f')
pgui.typewrite('"nan-qa-correct"')

sleep(.3)

answer_xy = pgui.locateOnScreen("img/nan-qa-correct.png", confidence=0.94)
x,y = pgui.center(answer_xy)

for _ in range(20):
    pgui.click(x + 60,y)
    pgui.click(x + 60,y)
    pgui.hotkey('ctrl', 'c')
    pgui.click(60,290)
    pgui.hotkey('ctrl', 'v')
    pgui.click(2400,430)
    pgui.click(2400,430)
    pgui.press("F12")
    pgui.hotkey('ctrl', 'f')
    pgui.typewrite('"nan-qa-correct"')
    sleep(.1)
    answer_xy = pgui.locateOnScreen("img/nan-qa-correct.png", confidence=0.94)
    x,y = pgui.center(answer_xy)

next = pgui.locateOnScreen("img/next.png", confidence=0.96)
print("Next Button Was Found -> CLICK")
pgui.click(next)