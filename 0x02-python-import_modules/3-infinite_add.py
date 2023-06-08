#!/usr/bin/python3


if __name__ == "__main__":
    """ print the sum of all args"""
    import sys

    total = 0
    count = len(sys.argv) - 1
    for i in range(count):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
