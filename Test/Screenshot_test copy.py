import pyautogui as pgui
import numpy as np
query = pgui.screenshot(region=(400, 270, 1600,260))
sc = pgui.screenshot(region=(1200, 630, 10,10))
img1 = pgui.screenshot(region=(700,570,450,100))
img2 = pgui.screenshot(region=(1170,570,450,100))
query.show()
sc.show()
img1.show()
img2.show()
