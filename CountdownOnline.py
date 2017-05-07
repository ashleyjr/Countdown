import time
import datetime
import cv2
from feed import feed
from still import still
from svc_frame import svc_frame

""" Constants """
current = "current.png"

def main():

    """ The frame classifier """
    svcf = svc_frame()
    svcf.load()

    """ Still handler """
    s = still()

    """ Start the feed off """
    f = feed()
    f.start()

    while(1):
        """ Load a still from the feed """
        s.load(f.take_still())

        print s.compress_make_linear()

        """ Classify """
        print svcf.is_frame(s.compress_make_linear())
        ts = time.time()
        stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S.jpg')
        s.save(stamp)

        time.sleep(2)


if __name__ == "__main__":
    main()
