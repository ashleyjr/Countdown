from threading import Thread
import time

class feed(Thread):
    def __init__(self):
        Thread.__init__(self)
        print "start"

    def take_still(self):
        print "still"

    def run(self):
        while(1):
            time.sleep(1)
            print "Hi"
