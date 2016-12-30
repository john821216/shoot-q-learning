import pyscreenshot as ImageGrab
import time
from threading import Thread
fileName=0

while True:
    im=ImageGrab.grab(bbox=(10,10,500,500))
    im.save(str(fileName) + '.png')
    fileName = fileName + 1
    if fileName == 10:
        fileName = 0
    time.sleep(1)