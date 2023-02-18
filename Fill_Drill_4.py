import pyautogui as pgui
from time import sleep
import numpy as np
from PIL import Image

ac = np.array([[[247, 152, 0] for _ in range(10)] for _ in range(10)])
blue = np.array([[[57, 180, 172] for _ in range(10)] for _ in range(10)])

for _ in range(1):
    while True:
        select_drill = pgui.locateOnScreen("img/drill.png", confidence=0.94)
        if select_drill == None:
            print("Drill Is Not Found -> DOWN")
            for _ in range(2):
                pgui.press("down")
        else:
            break
        sleep(1)
    print("Drill Was Found -> CLICK")
    x,y = pgui.center(select_drill)
    pgui.click(x - 100,y - 10)
    

    while True:
        start = pgui.locateOnScreen("img/start.png", confidence=0.95)
        if start == None:
            print("Start Button Is Not Found -> WAIT 1 SEC...")
            sleep(1)
        else:
            break
    print("Start Button Was Found -> CLICK")
    pgui.click(start)

    sleep(1)
    pgui.press("esc")

    while True:
        ok = pgui.locateOnScreen("img/ok.png", confidence=0.96)
        if ok == None:
            print("Ok Button Is Not Found -> WAIT 1 SEC...")
            sleep(1)
        else:
            break
    print("Ok Button Was Found -> CLICK")
    pgui.click(ok)

    sleep(1)
    
    query = []
    ans_img = []
    for i in range(20):
        while True:
            isnext = np.array(pgui.screenshot(region=(1130, 630, 10,10)))
            if np.array_equal(isnext,blue):
                break
            else:
                sleep(.1)
            
        print("case",i + 1,end = " : ")
        query.append(np.array(pgui.screenshot(region=(400, 270, 1600,260))).tolist())
        img1 = np.array(pgui.screenshot(region=( 750,570,400,100)))
        img2 = np.array(pgui.screenshot(region=(1175,570,400,100)))
        pgui.click(950,625)
        pgui.click(100,800)
        print("L",end = " ")
        sleep(.1)
        # 247,152,0 x 10 x 10
        choice = np.array(pgui.screenshot(region=(1130, 630, 10,10)))
        if np.array_equal(choice,ac):
            print("AC")
            ans_img.append(img1)
        else:
            print("WA")
            ans_img.append(img2)

        sleep(.5)
    while True:
        next = pgui.locateOnScreen("img/next.png", confidence=0.96)
        if not next == None:
            print("Next Button Was Found -> CLICK")
            pgui.click(next)
            break

        while True:
            isnext = np.array(pgui.screenshot(region=(1130, 630, 10,10)))
            if np.array_equal(isnext,blue):
                break
            else:
                sleep(.1)

        ques = np.array(pgui.screenshot(region=(400, 270, 1600,260)))
        ques_idx = query.index(ques.tolist())
        ans_xy = pgui.locateOnScreen(Image.fromarray(ans_img[ques_idx]),confidence=0.8)
        x,y = pgui.center(ans_xy)
        pgui.click(x,y)
        if x > 1160:
            print("R",end = " ")
            choice = np.array(pgui.screenshot(region=(1200, 630, 10,10)))
        else:
            print("L",end = " ")
            choice = np.array(pgui.screenshot(region=(1130, 630, 10,10)))
        if np.array_equal(choice,ac):
            print("AC")
        else:
            print("WA")
        sleep(.5)
