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

    """ Go through entire dataset and train """
    for i in range(0, d.len()):
        s.load(d.feature(i))
        feature = s.compress_make_linear()
        label = d.is_frame(i)
        svcf.train(feature, label)
        s.save(str(i) + ".png")


    """ Save ready for online processing """
    svcf.save()
    svcf.load()

    """ Go through entire dataset and check """
    for i in range(0, d.len()):
        s.load(d.feature(i))
        feature = s.compress_make_linear()
        label = d.is_frame(i)
        print str(i),
        if svcf.is_frame(feature) == d.is_frame(i):
            print "\tPASS: ",
        else:
            print "\tFAIL: ",
        print str(svcf.is_frame(feature)) + "\t\t" +  str(d.is_frame(i))

if __name__ == "__main__":
    main()
