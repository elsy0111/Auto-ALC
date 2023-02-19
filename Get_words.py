import pyautogui as pgui
from time import sleep
import numpy as np
import pyperclip
from PIL import Image
import codecs

ac = np.array([[[247, 152, 0] for _ in range(10)] for _ in range(10)])
blue = np.array([[[57, 180, 172] for _ in range(10)] for _ in range(10)])

for k in range(11,11 + 1):
    pgui.hotkey('ctrl', 'f')
    pgui.typewrite('UNIT' + str(k).zfill(3))
    while True:
        unit = pgui.locateOnScreen("img/unit.png", confidence=0.8)
        if unit == None:
            print("Unit Is Not Found -> Wait 200ms...")
            sleep(.2)
            pgui.hotkey('ctrl', 'f')
            pgui.typewrite('UNIT' + str(k).zfill(3))
        else:
            break
        sleep(1)
    print("Unit Was Found -> CLICK")
    x,y = pgui.center(unit)
    pgui.click(x + 300,y + 50)

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
    sleep(.2)

    no = pgui.locateOnScreen("img/no.png", confidence=0.96)
    if not no == None:
        pgui.click(no)

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
            isnext = np.array(pgui.screenshot(region=(1135, 578, 10,10)))
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
    br = 0
    while True:
        while True:
            isnext = np.array(pgui.screenshot(region=(1135, 578, 10,10)))
            if np.array_equal(isnext,blue):
                break
            else:
                next = pgui.locateOnScreen("img/next.png", confidence=0.96)
                if not next == None:
                    print("Next Button Was Found -> EXIT")
                    br = 1
                    break
                sleep(.1)
        if br:
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
    
    pgui.press("F12")
    sleep(.5)

    tag_xy = pgui.locateOnScreen("img/html_tag.png", confidence=0.95)
    pgui.rightClick(tag_xy)

    edit_xy = pgui.locateOnScreen("img/edit_html.png", confidence=0.95)
    pgui.click(edit_xy)

    pgui.hotkey('ctrl', 'a')
    pgui.hotkey('ctrl', 'c')

    pgui.press("F12")

    clip_str = pyperclip.paste()
    f = codecs.open('words/word_raw' + str(k) + '.txt', 'w',"utf-8")
    f.write(clip_str)
    f.close()

    pgui.hotkey('alt', 'f4')

    sleep(.3)
    leave_xy = pgui.locateOnScreen("img/leave.png", confidence=0.95)
    pgui.click(leave_xy)
