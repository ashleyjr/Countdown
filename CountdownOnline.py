import time
import cv2
from feed import feed
from still import still

""" Constants """
current = "current.png"

def main():

    """ Still handler """
    s = still()

    """ Start the feed off """
    f = feed()
    f.start()

    while(1):

        """ Take a still from the feed """
        im = f.take_still()

        """ Save the image to the disk """
        cv2.imwrite(current, im)

        """ Load a new image """
        s.load(current)

        """ Classify """
        print s.compress_make_linear()

if __name__ == "__main__":
    main()
