import pyscreenshot as ImageGrab
import time
import threading
import Queue
import cv2
import pyautogui
import numpy as np
from matplotlib import pyplot as plt

#capture location
X1 = 529
Y1 = 164
X2 = 905
Y2 = 853

SLEEPTIME =1.0 #1 second
MAXNUMBEROFFILENAME = 5
FRUITS = ['apple', 'greenApple', 'lemon', 'orange', 'wangcome', 'watermelon']

def screenCapture(MaxNumberOfFileName):
    curNumberOfFileName = 0
    while MaxNumberOfFileName > 0:
        #screen capture
        im = ImageGrab.grab(bbox=(X1, Y1, X2, Y2))
        #save pic 
        im.save("screenCapture/" +str(curNumberOfFileName) + '.png')
        #determine next pic's name
        curNumberOfFileName = curNumberOfFileName + 1
        MaxNumberOfFileName = MaxNumberOfFileName - 1
        time.sleep(SLEEPTIME)

def CV():
    for number in range(0, 1):
        gameImg = cv2.imread("screenCapture/" + str(number) +'.png',0)
        copyGameImg = gameImg.copy()

        for fruit in FRUITS:
            template = cv2.imread("fruit/" +str(fruit) +'.png',0)
            w, h = template.shape[::-1]
            gameImg = copyGameImg.copy()
            method = eval('cv2.TM_CCOEFF')
            res = cv2.matchTemplate(gameImg, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(gameImg,top_left, bottom_right, 255, 2)


            plt.subplot(121),plt.imshow(res)
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(gameImg)
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(fruit)
            plt.show()

            #the result we want
            print fruit
            print top_left 
            print bottom_right

def findMouseLocation():
    while True:
        print pyautogui.position()
        time.sleep(1)

#main 
#print "main about to start"
#time.sleep(2)
#print "start capturing pic"
#screenCapture(MAXNUMBEROFFILENAME)
CV()

#you can test where x1 x2 y1 y2 is using this function
#findMouseLocation()



