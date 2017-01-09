import numpy as np
import cv2
from sklearn import svm
from sklearn.externals import joblib

row_path = 'TestImages/TrainingRows/'
classifier_filename = 'tile_classifier.pkl'


def load_row(filename):
    img = cv2.imread(filename, 0)
    img = cv2.resize(img, (6*12, 12))
    ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
    return img


def break_row(im):
    """
    :param im: image of the numbers row
    :return: an array of 6 images
    """
    crops = []
    width, height = tuple(im.shape[1::-1])
    step = width/6
    for i in range(0, 6):
        start = i*step
        end = start + step
        crop = im[0:height, start:end]
        crops.append(crop)
    return crops


def main():
    classifier = joblib.load(classifier_filename)
    data_file = row_path + "/data.csv "
    data = np.genfromtxt(
        data_file,                                                          # file name
        skip_header=0,                                                      # lines to skip at the top
        skip_footer=0,                                                      # lines to skip at the bottom
        delimiter=',',                                                      # column delimiter
        dtype='int',                                                        # data type
        filling_values=0,                                                   # fill missing values with 0
        usecols=(0, 1, 2, 3, 4, 5, 6),                                      # columns to read
        names=['filename', 'one', 'two', 'three', 'four', 'five', 'six']    # column names
    )
    for i in range(0, len(data['filename'])):
        in_name = row_path + str(data['filename'][i]) + ".png"
        images = break_row(load_row(in_name))
        for j in range(0, 6):
            out_name = row_path + str(data['filename'][i]) + "_" + str(j) + ".png"
            cv2.imwrite(out_name, images[j])
            print classifier.predict(images[j].flatten())[0], data[i][j+1]

if __name__ == "__main__":
    main()
