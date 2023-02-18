import pyautogui as pgui
import numpy as np
sc = np.array(pgui.screenshot(region=(1155, 560, 10,10)))
pix = np.array([[[250, 188, 90] for _ in range(10)] for _ in range(10)])
if np.array_equal(sc,pix):
    print("SAME")
else:
    print("DIFFERENT")