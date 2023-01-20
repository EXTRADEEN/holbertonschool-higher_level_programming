#!/usr/bin/python3
import sys
if __name__ == "__main__":
    for i in range(0, len(sys.argv)):
        i = i + 1
    i = i - 1
    if i == 0:
        print("{} arguments.".format(i))
    else:
        print("{} arguments:".format(i))
    for a in range(0, len(sys.argv)):
        if a != 0:
            print("{}: {}".format(a, sys.argv[a]))
