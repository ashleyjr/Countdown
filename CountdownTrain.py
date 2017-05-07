from svc_frame import svc_frame
from dataset import dataset
from still import still


def main():
    """
        Begin training the classifiers using gathered training data
    """

    """ The frame classifier to be trained """
    svcf = svc_frame()

    """ Still handler """
    s = still()

    """ Load all the training data from know folder loaction """
    d = dataset()

    for i in range(0, d.len()):
        print i, d.is_frame(i)
        s.load(d.feature(i))
        feature = s.compress_make_linear()
        label = d.is_frame(i)
        svcf.train(feature, label)

if __name__ == "__main__":
    main()
