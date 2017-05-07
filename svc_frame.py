from sklearn import svm
from sklearn.externals import joblib
import numpy as np


""" Constants """
clf_filename = "svc_frame.svc"

class svc_frame():
    """
        Handle gathered data for training
    """

    def __init__(self):
        """
            Nothing loaded when initialised
        """
        self.features = []
        self.labels = []
        self.loaded = False;

    def load(self):
        """
            Load svc from the disk
        """
        self.clf = joblib.load(clf_filename)
        self.loaded = True

    def save(self):
        """
            Stash svc on disk
        """

        """ Nothing to save if nothing loaded """
        if not self.loaded:
            return

        """ Dumpe the loaded file """
        joblib.dump(self.clf, clf_filename)

    def train(self, feature, label):
        """
            Accumlate the training data and train
        """

        """ Start from scratch so anything loaded is destroyed """
        self.clf = svm.SVC(gamma=0.001)

        """ Label is true or false and must be turned in to a number """
        if label:
            num = 1
        else:
            num = -1

        """ Accumulate the data """
        self.features.append(feature)
        self.labels.append(num)

        """ Ensure both class are contained in the labes """
        if np.sum(self.labels) != len(self.labels):
            if np.sum(self.labels) != -len(self.labels):

                """ Fit the data, must be greater than one """
                self.clf.fit(self.features, self.labels)

                """ Now have an svc to save """
                self.loaded = True

    def is_frame(self, feature):
        """
            Use the svc to determine if the feature is a frame
        """
        if self.loaded:
            distance = self.clf.decision_function(feature.reshape(1, -1))
            print distance
            if distance > 0:
                return True
            else:
                return False



