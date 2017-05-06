from threading import Thread
import pyautogui
import cv2
import time

""" Constants """
temp = "temp.png"

class feed(Thread):
    """
        Access television feed and enable stills capture
    """

    def __init__(self):
        """
            Initalise the thread
        """

        """ Init inherited thread """
        Thread.__init__(self)

        """ Use gui interface to start the feed """
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

        """ Set the flag false as no image yet """
        self.take = False
        self.make = True

    def take_still(self):
        """
            Grab a still image from the threaded feed
        """

        while(1):
            if self.take:
                self.make = False
                img = self.shot
                self.make = True
                break
        return img

    def run(self):
        """
            Feed threaded
        """

        while(1):

            """ Take a screen shot """
            pyautogui.screenshot(temp)
            img = cv2.imread(temp, 1)
            width, height = tuple(img.shape[1::-1])
            img = img[int(height*0.31):int(height*0.775), int(width*0.26):int(width*0.73)]
            cv2.imwrite(temp, img)
            img = cv2.imread(temp, 1)

            """ Make sure last image is not being taken before making """
            while(1):
                if self.make:
                    self.take = False
                    self.shot = img
                    self.take = True
                    break

