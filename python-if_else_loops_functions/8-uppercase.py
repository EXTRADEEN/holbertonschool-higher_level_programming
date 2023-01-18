#!/usr/bin/python3
def uppercase(str):

    for i in str:
        i = ord(i)
        if i in range(97, 123):
            i = i - 32
        print("{:c}".format(i), end='')
    print()
