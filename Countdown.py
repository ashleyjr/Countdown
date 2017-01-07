import sys
import itertools


def op(op_code, nums, length):
    """ op_code, integer should be between 0 and 1023
        nums, list of numbers should be 6 long
        length, number of nums to use between 2 and 6
    """
    out = ""
    for i in range(1, length):
        out += "("
    base_two = bin(op_code)[2:]
    while 10 > len(base_two):
        base_two = "0" + base_two
    out += str(nums[0])
    accumulator = float(nums[0])
    for i in range(1, length):
        start = 2*(i-1)
        code = base_two[start:start+2]
        if "00" == code:
            out += "+"
            accumulator += float(nums[i])
        if "01" == code:
            out += "-"
            accumulator -= float(nums[i])
        if "10" == code:
            out += "*"
            accumulator *= float(nums[i])
        if "11" == code:
            out += "/"
            accumulator /= float(nums[i])
        out += str(nums[i]) + ")"
    return accumulator, out


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
    target = 1232
    finds = []
    perms = list(itertools.permutations(nums, len(nums)))
    top = len(perms)
    for perm in range(0, top):
        print (perm*100)/top
        for op_code in range(0, 1024):
            for length in range(2, 7):
                output, method = op(op_code, perms[perm], length)
                if target == sum:
                    find = method + " = " + str(output)
                    if find not in finds:
                        finds.append(find)
    for find in finds:
        print find

if __name__ == "__main__":
    main()
