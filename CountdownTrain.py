from dataset import dataset


def main():
    """
        Begin training the classifiers using gathered training data
    """

    d = dataset()
    d.load("data.zip")

if __name__ == "__main__":
    main()
