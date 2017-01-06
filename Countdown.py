import sys


def main():
    """ Main """

    """ Check correct number of arguments """
    if 6 >= len(sys.argv):
        print "Requires 6 arguments"
        return

    """ Attempt to turn arguments in array of integers """
    numbers = []
    for arg in sys.argv:
        try:
            numbers.append(int(arg))
        except ValueError:
            pass  # it was a string, not an int.

    print numbers

if __name__ == "__main__":
    main()
