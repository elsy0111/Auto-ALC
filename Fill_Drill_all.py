import pyautogui as pgui
from time import sleep
import numpy as np
from PIL import Image
import pyperclip

ac = np.array([[[247, 152, 0] for _ in range(10)] for _ in range(10)])
blue = np.array([[[57, 180, 172] for _ in range(10)] for _ in range(10)])

for _ in range(100):
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
        q = pgui.screenshot(region=(400, 270, 1600,260))
        # q.save("scr" + str(i + 1) + ".png")
        query.append(np.array(q).tolist())
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
    bre = 0
    while True:

        while True:
            isnext = np.array(pgui.screenshot(region=(1130, 630, 10,10)))
            if np.array_equal(isnext,blue):
                break
            else:
                next = pgui.locateOnScreen("img/next.png", confidence=0.93)
                if not next == None:
                    print("Next Button Was Found -> CLICK")
                    pgui.click(next)
                    bre = 1
                    break
                sleep(.1)
        if bre:
            bre = 0
            break

        ques = np.array(pgui.screenshot(region=(400, 270, 1600,260)))
        ques_idx = query.index(ques.tolist())
        ans_xy = pgui.locateOnScreen(Image.fromarray(ans_img[ques_idx]),confidence=0.8)
        x,y = pgui.center(ans_xy)
        pgui.click(x,y)
        pgui.click(100,800)
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


    while True:
        ok = pgui.locateOnScreen("img/ok.png", confidence=0.96)
        if ok == None:
            print("Ok Button Is Not Found -> WAIT 1 SEC...")
            sleep(1)
        else:
            break
    print("Ok Button Was Found -> CLICK")
    pgui.click(ok)

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

    sleep(1)

    next = pgui.locateOnScreen("img/next.png", confidence=0.96)
    print("Next Button Was Found -> CLICK")
    pgui.click(next)


    while True:
        ok = pgui.locateOnScreen("img/ok.png", confidence=0.96)
        if ok == None:
            print("Ok Button Is Not Found -> WAIT 1 SEC...")
            sleep(1)
        else:
            break
    print("Ok Button Was Found -> CLICK")
    pgui.click(ok)

    for _ in range(7):
        a_xy = pgui.locateOnScreen("img/A.png", confidence=0.8)
        pgui.click(a_xy)
        
    for _ in range(16):
        pgui.press("down")

    for _ in range(3):
        a_xy = pgui.locateOnScreen("img/A.png", confidence=0.8)
        pgui.click(a_xy)

    pgui.click(2400,430)

    sleep(1)

    next = pgui.locateOnScreen("img/next.png", confidence=0.96)
    print("Next Button Was Found -> CLICK")
    pgui.click(next)


    while True:
        ok = pgui.locateOnScreen("img/ok.png", confidence=0.96)
        if ok == None:
            print("Ok Button Is Not Found -> WAIT 1 SEC...")
            sleep(1)
        else:
            break

    print("Ok Button Was Found -> CLICK")
    pgui.click(ok)

    pgui.press("F12")
    sleep(.1)
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
    pgui.press("F12")

    while True:
        sleep(.3)
        goal = pgui.locateOnScreen("img/goal2.png", confidence=0.96)
        if not goal == None:
            print("Goal Button Was Found -> CLICK")
            pgui.click(goal)
            break

        while True:
            isnext = np.array(pgui.screenshot(region=(1130, 630, 10,10)))
            if np.array_equal(isnext,blue):
                break
            else:
                sleep(.1)
        q = pgui.screenshot(region=(400, 270, 1600,260))
        ques = np.array(q)
        try:
            ques_idx = query.index(ques.tolist())
        except:
            continue
        ans_xy = pgui.locateOnScreen(Image.fromarray(ans_img[ques_idx]),confidence=0.8)
        try:
            x,y = pgui.center(ans_xy)
        except:
            continue
        pgui.click(x,y)
        pgui.click(100,800)
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
        sleep(.8)

    while True:
        yes = pgui.locateOnScreen("img/yes.png", confidence=0.96)
        if yes == None:
            print("Yes Is Not Found -> WAIT 0.5 SEC...")
            sleep(.5)
        else:
            break
    print("Yes Was Found -> CLICK")
    pgui.click(yes)