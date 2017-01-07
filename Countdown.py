import sys


def num_op(op, one, two):
    if 0 == op:
        return one + two
    if 1 == op:
        return one - two
    if 2 == op:
        return one * two
    if 3 == op:
        return one / two


def print_op(op):
    if 0 == op:
        return "+"
    if 1 == op:
        return "-"
    if 2 == op:
        return "*"
    if 3 == op:
        return "/"


def str_setup(ops, nums):
    print "(((((",
    if ops[0]:
        print



    for i in range(0, 5):
        print str(nums[i]) + " ) " + str(print_op(ops[i])) + " ",
    return str(nums[5])


def main():
    """ Main """

    """ Check correct number of arguments """
    if 7 != len(sys.argv):
        print "Requires 6 numbers"
        return

    """ Attempt to turn arguments in array of integers """
    nums = []
    for i in range(1, 7):
        try:
            nums.append(int(sys.argv[i]))
        except ValueError:
            print "All arguments must be numbers"
            return

    """ Run the hill climber """
    ops = [0, 0, 0, 0, 0]
    for length in range(2, 7):
        for i in range(2, length):
            sys.stdout.write("(")
        accumulator = num_op(ops[0], nums[0], nums[1])
        sys.stdout.write("(" + str(nums[0]) + print_op(ops[0]) + str(nums[1]) + ")")
        for i in range(2, length):
            accumulator = num_op(ops[i - 1], accumulator, nums[i])
            sys.stdout.write(print_op(ops[0]) + str(nums[i]) + ")")
        sys.stdout.write(" = " + str(accumulator) + "\n")


if __name__ == "__main__":
    main()
