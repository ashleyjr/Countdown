import cv2

class still():
    """
        Handle tasks related to the single frame
    """

    def __init__(self):
        """ No image loaded to start """
        self.loaded = False

    def load(self, path):
        """
            Use a path to load an image from the disk
        """

        self.loaded = True

    def save(self, path):
        """
            Write the raw image to the disk
        """

        """ Bail if no image loaded """
        if not self.loaded:
            return

    def compress_make_linear(self):
        """
            Prepare the image for the classifier
        """

        """ Bail if no image loaded """
        if not self.loaded:
            return

    def segment(self):
        """
            Dig out the segments of interest in the image
        """

        """ Bail if no image loaded """
        if not self.loaded:
            return

