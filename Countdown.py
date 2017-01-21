import os
import zipfile
import cv2
import numpy as np
from sklearn import svm
from sklearn import cross_validation
import matplotlib.pyplot as plt


""" Global constants """
data_zip = "data.zip"               # The zip archive
clean_files = [".csv", ".jpg"]      # File extensions to clean
data_file = "data.csv"
img_ext = ".jpg"
perf_file = "performance.txt"


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
    #img = cv2.Canny(img, 100, 200)
    ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
    return img


def main():
    unzip_data()

    labels = []

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

    """ The features """
    x = 3
    y = 12
    bottom = 0.15
    features = []
    for name in data['filename']:
        name_ext = str(name) + img_ext
        im = downscale_image(cv2.imread(name_ext, 0), bottom, x, y)
        img = cv2.resize(im, (100 * x, 100 * y))
        features.append(im.flatten())

    """ Train and validate the classifier """
    loops = 300
    acc = 0
    mean = []
    for i in range(1, loops):
        """ Split data for cross validation """
        features_train, features_test, labels_train, labels_test = \
            cross_validation.train_test_split(features, labels, test_size=0.1, random_state=i)

        """ Train """
        clf = svm.SVC(gamma=0.001)
        clf.fit(features_train, labels_train)

        """ Score """
        acc += clf.score(features_test, labels_test)
        mean.append(acc/i)

    """ Write performance to file to keep track """
    f = open(perf_file, 'w')
    f.write("Performance: " + str(mean[-1]))
    f.close()

    """ Train on all the data """
    clf = svm.SVC(gamma=0.001)
    clf.fit(features, labels)

    """ Find good images """
    x = 3
    y = 12
    bottom = 0.15
    for name in data['filename']:
        name_ext = str(name) + img_ext
        im = downscale_image(cv2.imread(name_ext, 0), bottom, x, y)
        if 1 == clf.predict(im.flatten()):
            print name


    """ remove temp data """
    clean_data()

    """ Ensure the mean has converged """
    plt.plot(mean)
    plt.show()      # WILL STALL HERE

if __name__ == "__main__":
    main()
