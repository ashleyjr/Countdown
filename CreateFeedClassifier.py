import os
import zipfile
import cv2
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn.externals import joblib
import matplotlib.pyplot as plt

""" Tunes """
x = 6
y = 6
bottom = 0.4

""" Global constants """
data_zip = "data.zip"               # The zip archive
clean_files = [".csv", ".jpg"]      # File extensions to clean
data_file = "data.csv"
img_ext = ".jpg"
perf_file = "performance.txt"


def main():
    """ Unzip the data held in zip file """
    zip_ref = zipfile.ZipFile(data_zip, 'r')
    zip_ref.extractall('')
    zip_ref.close()

    """ Load data  """
    data = np.genfromtxt(
        data_file,                      # file name
        skip_header=0,                  # lines to skip at the top
        skip_footer=0,                  # lines to skip at the bottom
        delimiter=',',                  # column delimiter
        dtype='int',                    # data type
        filling_values=0,               # fill missing values with 0
        usecols=(0, 1, 2, 3, 4, 5, 6),  # columns to read
        names=[
            'filename',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six'
        ]                               # column names
    )

    """ The labels """
    labels = []
    for ones in data['one']:
        if ones:
            labels.append(1)
        else:
            labels.append(-1)

    """ The features """
    features = []
    for name in data['filename']:
        """ Load the image """
        name_ext = str(name) + img_ext
        img = cv2.imread(name_ext, 0)
        """ Take bottom section"""
        width, height = tuple(img.shape[1::-1])
        img = img[int(round((1 - bottom) * (height - 1))):(height - 1), 1:(width - 1)]
        bottom_ext = str(name) + "_bottom_"+ img_ext
        cv2.imwrite(bottom_ext,img)
        """ Scale down """
        img = cv2.resize(img, (x, y))
        ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
        scale_ext = str(name) + "_scale_"+ img_ext
        """ Scale back up only to save """
        cv2.imwrite(scale_ext,cv2.resize(img, (100*x, 100*y)))
        """ Add to list of training features """
        features.append(img.flatten())

    """ Train on all the data """
    clf = svm.SVC(gamma=0.001)
    clf.fit(features, labels)

    """ Save the classifier """
    joblib.dump(clf, "FeedClassifier.clf")

    """ Decision function """
    distances = clf.decision_function(features)

    """ False positives and negatives, look out for uncertainity """
    for i in range(0,len(distances)):
        print i+1,distances[i],
        if labels[i] > 0:
            if distances[i] < 0:
                print "\t\tFALSE NEGATIVE",
            else:
                print "\t\tPOSITIVE",
        else:
            if distances[i] > 0:
                print "\t\tFALSE POSITIVE",
            else:
                print "\t\tNEGATIVE",
        uncertainity = abs(distances[i])
        print "\t\t",
        while uncertainity > 0:
            print "-",
            uncertainity -= 0.1
        print " "

    """ Clean up all the temp data """
    #for clean_file in clean_files:
    #    file_list = [f for f in os.listdir(".") if f.endswith(clean_file)]
    #    for f in file_list:
    #        os.remove(f)


if __name__ == "__main__":
    main()
