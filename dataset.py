import zipfile
import numpy as np
import cv2
import os

""" Constants """
data_zip = "data.zip"
data_file = "data.csv"
img_ext = ".jpg"

class dataset():
    """
        Handle gathered data for training
    """

    def __init__(self):
        """
            Load all training images and labels
        """

        """ Unzip the folder containing the data """
        zip_ref = zipfile.ZipFile(data_zip, 'r')
        zip_ref.extractall('')
        zip_ref.close()

        """ Load label data from csv file  """
        data = np.genfromtxt(
            data_file,                          # file name
            skip_header=0,                      # lines to skip at the top
            skip_footer=0,                      # lines to skip at the bottom
            delimiter=',',                      # column delimiter
            dtype='int',                        # data type
            filling_values=0,                   # fill missing values with 0
            usecols=(0, 1, 2, 3, 4, 5, 6, 7),   # columns to read
            names=[
                'filename',
                'one',
                'two',
                'three',
                'four',
                'five',
                'six',
                'target'
            ]                               # column names
        )

        """ Crete arrays for training data """
        self.images = []
        self.labels = []

        """ Loop over elements in the set """
        for i in range(0, len(data['filename'])):

            """ Load image and place in array """
            name_ext = str(data['filename'][i]) + img_ext
            self.images.append(cv2.imread(name_ext, 0))
            print name_ext

            """ Delete the extracted image now loaded """
            os.remove(name_ext)

            """ Place the labels in array """
            temp = []
            temp.append(data['one'][i])
            temp.append(data['two'][i])
            temp.append(data['three'][i])
            temp.append(data['four'][i])
            temp.append(data['five'][i])
            temp.append(data['six'][i])
            temp.append(data['target'][i])
            self.labels.append(temp)

    def len(self):
        """
            The length of the dataset
        """
        return len(self.images)

    def pattern(self, index):
        """
            Return a single index in the dataset
        """
        return self.images[index], self.labels[index]
