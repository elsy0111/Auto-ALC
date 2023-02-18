import pyautogui as pgui
from time import sleep

for _ in range(10):
    a_xy = pgui.locateOnScreen("img/A.png", confidence=0.8)
    pgui.click(a_xy)
    pgui.press("down")
    pgui.press("down")
    pgui.press("down")

pgui.click(2400,430)
sleep(1)

next = pgui.locateOnScreen("img/next.png", confidence=0.96)
print("Next Button Was Found -> CLICK")
pgui.click(next)