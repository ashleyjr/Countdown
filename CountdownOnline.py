import time
import cv2
from feed import feed

""" Constants """
current = "current.png"

def main():

    """ Start the feed off """
    f = feed()
    f.start()

    while(1):

        """ Take a still from the feed """
        im = f.take_still()

        """ Save the image to the disk """
        cv2.imwrite(current, im)

if __name__ == "__main__":
    main()
