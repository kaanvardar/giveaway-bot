#to do task initially
#set screen size:1920x1080
#set zoom=75
#472 12/04/2023

import sys
import pyautogui 
import time 
import random

infinite_counter = 1
click_counter = 0
joined_giveaway = 0

#pyautogui.displayMousePosition()

while (infinite_counter < 2):

    pyautogui.moveTo(1451,919)      #outer click
    time.sleep(3)
    pyautogui.click(button='left', clicks=1, interval=0.50)
    click_counter +=1
    
    pyautogui.moveTo(631,786)       #inner click
    time.sleep(3)
    pyautogui.click(button='left', clicks=1, interval=0.50)
    time.sleep(10)                   #second inner clock for 10s warning
    pyautogui.click(button='left', clicks=1, interval=0.50)    
    click_counter +=1
    
    pyautogui.moveTo(424,857)       #not robot
    time.sleep(3)
    pyautogui.click(button='left', clicks=1, interval=0.50)
    click_counter +=1
    
    pyautogui.moveTo(421,52)       #go to site
    #time.sleep(3)
    pyautogui.click(button='left', clicks=1, interval=0.50)
    pyautogui.typewrite('https://key-drop.com/tr/giveaways/list', interval=0.50)
    pyautogui.typewrite(['enter'], interval=0.50)
    click_counter+=1
    
    pyautogui.moveTo(87,60)         #refresh page
    pyautogui.click(button='left', clicks=1, interval=2)
    click_counter +=1
    
    time.sleep(20)                  #wait for giveaway
    
    pyautogui.moveTo(87,60)         #refresh page
    time.sleep(3)
    pyautogui.click(button='left', clicks=1, interval=0.50)
    click_counter +=1
    joined_giveaway = click_counter / 6

    result = 'joined giveaway is: ' +str(joined_giveaway)
    print(result)


#go to site
#x=421
#y=52
#left click -> type site url -> press enter

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