import os
from PIL import Image
from sklearn import datasets, svm, metrics
from sklearn.externals import joblib

filename = 'tile_classifier'
scale = 50, 50
threshold = 128
classifier = svm.SVC(gamma=0.001)


def load_im_array(path):
    im = Image.open(path)
    im = im.resize(scale, Image.ANTIALIAS).convert('L')
    im = im.point(lambda x: 0 if x < threshold else 1, '1')
    return list(im.getdata())


""" Train the SVC """
features = []
samples = []
training_path = 'TestImages/TrainingNumbers/'
for i in range(1, 101):
    j = 1
    while True:
        number = training_path + "/" + str(i) + "_" + str(j) +".png"
        if os.path.isfile(number):
            features.append(load_im_array(number))
            samples.append(i)
        else:
            break
        j += 1
print features
print samples
classifier.fit(features, samples)

joblib.dump(classifier, 'file.pkl')


""" Test the SVC """
testing_path = 'TestImages/TestingNumbers/'
for i in range(1, 101):
    number = testing_path + "/" + str(i) + "_1.png"
    if os.path.isfile(number):
        output = classifier.predict(load_im_array(number))
        if i == output:
            print "PASS",
        else:
            print "FAIL",
        print ": Image is " + str(i) + ", SVC returned " + str(output[0])
