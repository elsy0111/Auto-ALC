import pyautogui as pgui
from time import sleep


for _ in range(100):
    while True:
        select_input = pgui.locateOnScreen("img/input.png", confidence=0.94)
        if select_input == None:
            print("Input Button Is Not Found -> DOWN")
            for _ in range(2):
                pgui.press("down")
        else:
            break
        sleep(1)
    print("Input Button Was Found -> CLICK")
    x,y = pgui.center(select_input)
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

    sleep(20)

    while True:
        goal = pgui.locateOnScreen("img/goal.png", confidence=0.96)
        if goal == None:
            print("Goal Button Is Not Found -> WAIT 1 SEC...")
            sleep(1)
        else:
            break
    print("Goal Button Was Found -> CLICK")
    pgui.click(goal)

    while True:
        yes = pgui.locateOnScreen("img/yes.png", confidence=0.96)
        if yes == None:
            print("Yes Is Not Found -> WAIT 0.5 SEC...")
            sleep(.5)
        else:
            break
    print("Yes Was Found -> CLICK")
    pgui.click(yes)
    
    sleep(5)

    for _ in range(4):
        pgui.press("up")