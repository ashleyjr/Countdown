import sys
import random


def num_op(op, one, two):
    if 0 == op:
        return float(one) + float(two)
    if 1 == op:
        return float(one) - float(two)
    if 2 == op:
        return float(one) * float(two)
    if 3 == op:
        return float(one) / float(two)


def print_op(op):
    if 0 == op:
        return "+"
    if 1 == op:
        return "-"
    if 2 == op:
        return "*"
    if 3 == op:
        return "/"


def rand_ops():
    ops = []
    for i in range(0, 6):
        ops.append(int(round(random.random()*3)))
    return ops


def shuffle(in_nums):
    out_nums = []
    for i in range(0, 6):
        rand_pos = int(round(random.random()*(len(in_nums)-1)))
        out_nums.append(in_nums[rand_pos])
        del in_nums[rand_pos]
    return out_nums


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
    finds = []
    target = 200
    for trys in range(0, 100000):
        print trys
        nums = shuffle(nums)
        ops = rand_ops()
        for length in range(2, 7):
            find = ""
            for i in range(2, length):
                find += "("
            accumulator = num_op(ops[0], nums[0], nums[1])
            find += "(" + str(nums[0]) + print_op(ops[0]) + str(nums[1]) + ")"
            for i in range(2, length):
                accumulator = num_op(ops[i - 1], accumulator, nums[i])
                find += print_op(ops[i - 1]) + str(nums[i]) + ")"
            find += " = " + str(accumulator) + "\n"
            if target == accumulator:
                if find not in finds:
                    finds.append(find)
    for eq in finds:
        print eq

if __name__ == "__main__":
    main()
