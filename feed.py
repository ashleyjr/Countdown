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
import threading

def update():
    """ Time stamp and file names"""
    timestamp = time.strftime("%H_%M_%S")
    data = "feed/data.csv"
    temp = "temp.png"
    trigger = "feed/" + timestamp + "_trigger.png"
    bottom = "feed/" + timestamp + "_bottom.png"
    downscale = "feed/" + timestamp + "_downscale.png"
    zipped = "feed/" + timestamp + ".zip"

    """ Capture the image"""
    pyautogui.screenshot(temp)
    img = cv2.imread(temp, 1)
    width, height = tuple(img.shape[1::-1])
    img = img[int(height*0.31):int(height*0.775), int(width*0.26):int(width*0.73)]
    cv2.imwrite(trigger, img)

    """ Take the bottom part of the image """
    img = cv2.imread(trigger, 0)
    width, height = tuple(img.shape[1::-1])
    img = img[int(round(0.85 * (height - 1))):(height - 1), 1:(width - 1)]
    cv2.imwrite(bottom, img)

    """ Scale down the bottom part of the image and threshold """
    img = cv2.resize(img, (3, 12))
    ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)

    """ Load and classify the image """
    clf = joblib.load("bottom.clf")
    classify = clf.predict(img.flatten())

    """ Record the data """
    if os.path.isfile(data):
        f = open(data,'a')
    else:
        f = open(data,'w+')
    f.write(timestamp + ",")
    if int(classify[0]) < 0:
        f.write("FALSE\n\r")
    else:
        f.write("-----------TRUE\n\r")
    f.close()

    """ Scale up the input to the classifier """
    img = cv2.resize(img, (300, 1200))
    cv2.imwrite(downscale, img)


    """ Zip up files and delete temp files """
    zipper = zipfile.ZipFile(zipped, 'w')
    zipper.write(trigger, compress_type=zipfile.ZIP_DEFLATED)
    zipper.write(bottom, compress_type=zipfile.ZIP_DEFLATED)
    zipper.write(downscale, compress_type=zipfile.ZIP_DEFLATED)
    zipper.close()
    os.remove(temp)
    os.remove(trigger)
    os.remove(bottom)
    os.remove(downscale)


    """ Call again in 10 minutes"""
    t = threading.Timer(10, update)
    t.start()



def main():

    """ Set up the screen caps"""
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

    """ Timer """
    update()

    """ Keep alove for thread """
    while(1):
        pass

if __name__ == "__main__":
    main()
