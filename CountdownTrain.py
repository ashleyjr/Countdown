from dataset import dataset


def main():
    """
        Begin training the classifiers using gathered training data
    """

    """ Load all thr training data from know folder loaction """
    d = dataset()

    print d.len()
    print d.pattern(1)

if __name__ == "__main__":
    main()
