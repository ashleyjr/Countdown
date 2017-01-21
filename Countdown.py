import os
import zipfile
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import cross_validation

""" Global constants """
data_zip = "data.zip"               # The zip archive
clean_files = [".csv", ".jpg"]      # File extensions to clean
data_file = "data.csv"
img_ext = ".jpg"


def unzip_data():
    """ Unzip the data held in zip file """
    zip_ref = zipfile.ZipFile(data_zip, 'r')
    zip_ref.extractall('')
    zip_ref.close()


def clean_data():
    """ Clean up all the unzipped data """
    for clean_file in clean_files:
        file_list = [f for f in os.listdir(".") if f.endswith(clean_file)]
        for f in file_list:
            os.remove(f)


def downscale_image(img, bottom, x, y):
    """
        Take bottom section of image
        Rescale
        Canny edge detection
    """
    width, height = tuple(img.shape[1::-1])
    img = img[int(round((1 - bottom) * (height - 1))):(height - 1), 1:(width - 1)]
    img = cv2.resize(img, (x, y))
    img = cv2.Canny(img, 100, 200)
    return img


def main():
    unzip_data()

    labels = []
    features = []

    """ The labels """
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
    for ones in data['one']:
        if ones:
            labels.append(1)
        else:
            labels.append(-1)

    """ The data """
    for name in data['filename']:
        name_ext = str(name) + img_ext
        im = downscale_image(cv2.imread(name_ext, 0), 0.2, 100, 10)
        features.append(im.flatten())

    loops = 1500
    mean = 0
    meantime = []
    for i in range(1,loops):
        """ Split data for cross validation """
        features_train, features_test, labels_train, labels_test = \
            cross_validation.train_test_split(features, labels, test_size=0.1, random_state=i)

        """ Train """
        clf = svm.SVC(gamma=0.001)
        clf.fit(features_train, labels_train)

        """ Score """
        mean += clf.score(features_test, labels_test)
        meantime.append(mean/i)

    plt.plot(meantime)
    plt.show()

    clean_data()

if __name__ == "__main__":
    main()
