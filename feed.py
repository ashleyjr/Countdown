import pyautogui
import time
import os
import zipfile
import cv2
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import shutil



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
if os.path.exists("feed"):
    shutil.rmtree('feed')
os.mkdir("feed")
while(True):
    """ Lower the frame rate"""
    time.sleep(10)

    """ Capture the image"""
    timestamp = time.strftime("%H_%M_%S")
    temp = timestamp + ".png"
    pyautogui.screenshot(temp)
    img = cv2.imread(temp, 1)
    os.remove(temp)
    width, height = tuple(img.shape[1::-1])
    img = img[int(height*0.31):int(height*0.775), int(width*0.26):int(width*0.73)]
    cv2.imwrite("feed/" + timestamp + "_A_trigger.png", img)

    """ Take the bottom part of the image """
    img = cv2.imread("feed/" + timestamp + "_A_trigger.png", 0)
    width, height = tuple(img.shape[1::-1])
    img = img[int(round(0.85 * (height - 1))):(height - 1), 1:(width - 1)]
    cv2.imwrite("feed/" + timestamp + "_B_bottom.png", img)

    """ Scale down the bottom part of the image and threshold """
    img = cv2.resize(img, (3, 12))
    ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)

    """ Load and classify the image """
    clf = joblib.load("bottom.clf")
    if clf.predict(img.flatten()) > 0:
        f = open("feed/A_TRIGGERED_" + timestamp + ".txt",'w')
        f.close()
    else:
        f = open("feed/B_NOT_TRIGGERED_" + timestamp + ".txt",'w')
        f.close()

    """ Scale up the input to the classifier """
    img = cv2.resize(img, (300, 1200))
    cv2.imwrite("feed/" + timestamp + "_C_downscale.png", img)

