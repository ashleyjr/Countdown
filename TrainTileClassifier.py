import os
import cv2
from PIL import Image, ImageFilter
from sklearn import svm
from sklearn.externals import joblib


def main():
    filename = 'tile_classifier.pkl'
    training_path = 'TestImages/TrainingNumbers/'
    scale = 20, 20
    threshold = 128
    classifier = svm.SVC(gamma=0.001)
    features = []
    samples = []
    for i in range(1, 101):
        j = 1
        while True:
            number = training_path + "/" + str(i) + "_" + str(j) + ".png"
            if os.path.isfile(number):
                img = cv2.imread(number, 0)
                edges = cv2.Canny(img, 100, 200)
                edges = cv2.resize(edges, (50, 50))
                cv2.imwrite(training_path + "/canny_" + str(i) + "_" + str(j) + ".png", edges)
            else:
                break
            j += 1
    for i in range(1, 101):
        j = 1
        while True:
            number = training_path + "/" + str(i) + "_" + str(j) + ".png"
            if os.path.isfile(number):
                im = Image.open(number)
                im = im.resize(scale, Image.ANTIALIAS).convert('L')
                im = im.filter(ImageFilter.FIND_EDGES)
                im = im.point(lambda x: 0 if x < threshold else 255, '1')
                #im.show()
                features.append(list(im.getdata()))
                samples.append(i)
            else:
                break
            j += 1
    classifier.fit(features, samples)
    joblib.dump(classifier, filename)

if __name__ == "__main__":
    main()
