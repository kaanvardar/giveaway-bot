#screen size:1920x1080
#zoom=75
#for LARGER giveaway bot

import pyautogui 
import time 
import random

#pyautogui.displayMousePosition()


while True:
    
    pyautogui.moveTo(1229,918)      #outer click
    time.sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(525,781)       #inner click
    time.sleep(1)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(424,857)       #not robot
    time.sleep(3)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(25,50)         #backspace
    time.sleep(1)
    pyautogui.click(button='left', clicks=1, interval=0.50)

    pyautogui.moveTo(87,60)         #refresh page
    pyautogui.click(button='left', clicks=1, interval=0.50)
    

    time.sleep(70)                  #wait for giveaway


    pyautogui.moveTo(87,60)         #refresh page
    pyautogui.click(button='left', clicks=1, interval=0.50)


#outer_join
#x=1229
#y=918

#inner_join
#x=525
#y=781

#backspace
#x=25
#y=50

#outer_join2
#x=1451
#y=919

#inner_join2
#x=631
#y=786

#refresh
#x=87
#y=60

#not robot
#x=424
#y=857