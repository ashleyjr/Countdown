import cv2

""" constants """
x = 5
y = 12
bottom = 0.4


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
        self.im = cv2.imread(path, 1)
        self.loaded = True

    def save(self, path):
        """
            Write the raw image to the disk
        """

        """ Bail if no image loaded """
        if not self.loaded:
            return

        """ save the image to the disk """
        cv2.imwrite(path, self.im)

    def compress_make_linear(self):
        """
            Prepare the image for the classifier
        """

        """ Bail if no image loaded """
        if not self.loaded:
            return

        """ Take bottom section"""
        width, height = tuple(self.im.shape[1::-1])
        im  = self.im[int(round((1 - bottom) * (height - 1))):(height - 1), 1:(width - 1)]

        """ Scale down """
        im = cv2.resize(im, (x, y))

        """ Threshold against the mean """
        ret, im = cv2.threshold(im, im.mean(), 255, cv2.THRESH_BINARY)

        """ Return the flattened image """
        return im.flatten()


    def segment(self):
        """
            Dig out the segments of interest in the image
        """

        """ Bail if no image loaded """
        if not self.loaded:
            return

