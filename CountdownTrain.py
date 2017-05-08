import time
from svc_frame import svc_frame
from dataset import dataset
from still import still
from sklearn import cross_validation

def main():
    """
        Begin training the classifiers using gathered training data
    """

    good = 0
    bad = 0
    for i in range(0, 10):

        """ The frame classifier to be trained """
        svcf = svc_frame()

        """ Still handler """
        s = still()

        """ Load all the training data from know folder loaction """
        d = dataset()

        """ Create training set """
        features = []
        labels = []
        for i in range(0, d.len()):
            s.load(d.feature(i))
            features.append(s.compress_make_linear())
            labels.append(d.is_frame(i))

        """ Split for validiation """
        features_train, features_test, labels_train, labels_test = \
            cross_validation.train_test_split(features, labels, test_size=0.2, random_state=int(time.time()))

        """ Train """
        for i in range(0, len(features_train)):
            svcf.train(features_train[i], labels_train[i])

        """ Validate """
        for i in range(0, len(features_test)):
            if svcf.is_frame(features_test[i]) == labels_test[i]:
                good += 1
            else:
                bad += 1

        print good, bad

if __name__ == "__main__":
    main()
