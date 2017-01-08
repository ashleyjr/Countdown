import os
from PIL import Image
from sklearn import svm
from sklearn.externals import joblib


def main():
    filename = 'tile_classifier.pkl'
    training_path = 'TestImages/TrainingNumbers/'
    scale = 50, 50
    threshold = 128
    classifier = svm.SVC(gamma=0.001)
    features = []
    samples = []
    for i in range(1, 101):
        j = 1
        while True:
            number = training_path + "/" + str(i) + "_" + str(j) + ".png"
            if os.path.isfile(number):
                im = Image.open(number)
                im = im.resize(scale, Image.ANTIALIAS).convert('L')
                im = im.point(lambda x: 0 if x < threshold else 1, '1')
                features.append(list(im.getdata()))
                samples.append(i)
            else:
                break
            j += 1
    classifier.fit(features, samples)
    joblib.dump(classifier, filename)

if __name__ == "__main__":
    main()
