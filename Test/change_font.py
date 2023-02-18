import pyautogui as pgui
import pyperclip
from time import sleep

pgui.press("F12")
sleep(.5)
pgui.hotkey('ctrl', 'f')
pgui.typewrite('nan-vocabulary-inline')

sleep(.2)
anchour_xy = pgui.locateOnScreen("img/nan-vocabulary-inline.png", confidence=0.9)
pgui.click(anchour_xy)
pgui.click(anchour_xy)

pgui.press("esc")
pgui.press("down")
pgui.press("down")

font_xy = pgui.locateOnScreen("img/change_font.png", confidence=0.9)

sleep(.2)
pgui.click(font_xy)
pgui.click(font_xy)

pyperclip.copy('font-size: 115px; line-height: 1.2em;')

pgui.hotkey('ctrl', 'v')
pgui.press("enter")