import os
from PIL import Image
from sklearn import datasets, svm, metrics
from sklearn.externals import joblib

row_path = 'TestImages/TestingRows/'
scale = 50, 50
threshold = 128

classifier = joblib.load('tile_classifier.pkl')
for f in os.listdir(row_path):
    im = Image.open(row_path + f)
    width, height = im.size
    step = width/6
    for i in range(0, 6):
        crop_rectangle = ((step*i), 0, (step*(i+1)), height)
        cropped_im = im.crop(crop_rectangle)
        cropped_im = cropped_im.resize(scale, Image.ANTIALIAS).convert('L')
        cropped_im = cropped_im.point(lambda x: 0 if x < threshold else 255, '1')
        cropped_im.show()
        print classifier.predict(list(cropped_im.getdata()))
    im.show()
