import sys


def operation(op, one, two):
    if 0 == op:
        return 0
    if 1 == op:
        return one + two
    if 2 == op:
        return one - two
    if 3 == op:
        return one * two
    if 4 == op:
        return one / two


def print_op(op):
    if 0 == op:
        return ""
    if 1 == op:
        return "+"
    if 2 == op:
        return "-"
    if 3 == op:
        return "*"
    if 4 == op:
        return "/"


def str_setup(ops, nums):
    print "(((((",
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
    numbers = []
    for i in range(1, 7):
        try:
            numbers.append(int(sys.argv[i]))
        except ValueError:
            print "All arguments must be numbers"
            return

    operations = [1, 1, 1, 1, 1]
    accumulator = numbers[0]
    for i in range(0, 5):
        accumulator = operation(operations[i], accumulator, numbers[i+1])
    print str_setup(operations, numbers) + " = " + str(accumulator)

if __name__ == "__main__":
    main()
