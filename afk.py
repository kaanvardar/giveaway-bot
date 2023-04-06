#screen size:1920x1080
#zoom=75

import pyautogui 
import time 
import random

pyautogui.displayMousePosition()

while True:
    pyautogui.moveTo(1229,918)
    time.sleep(1)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(525,781)
    time.sleep(1)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(25,50)
    time.sleep(1)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(87,60)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(1453,957)
    time.sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(631,786)
    time.sleep(1)
    pyautogui.click(button='left', clicks=1, interval=0.50)
    

""""
pyautogui.moveTo(1000,50)
time.sleep(3)
pyautogui.moveTo(1000,100)

outer_join
x=1229
y=918

inner_join
x=525
y=781

backspace
x=25
y=50

outer_join2
x=1453
y=927

inner_join2
x=631
y=786


refresh
x=87
y=60
pyautogui.click(button='right', clicks=3, interval=0.25)

"""