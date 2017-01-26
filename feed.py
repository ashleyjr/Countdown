import pyautogui
import time
import os
import zipfile
import cv2
import numpy as np
from sklearn import svm
from sklearn import cross_validation
import matplotlib.pyplot as plt
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.moveTo(160,750)
pyautogui.click()
time.sleep(2)
pyautogui.click(400,50)
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')
pyautogui.typewrite('http://tvcatchup.com/watch/channel4')
pyautogui.press('enter')
while(True):
    name = time.strftime("%H_%M_%S") + ".png"
    pyautogui.screenshot(name)
    img = cv2.imread(name, 0)
    width, height = tuple(img.shape[1::-1])
    img = img[int(height*0.2):int(height*0.8), int(width*0.2):int(width*0.8)]
    cv2.imwrite(name, img)

