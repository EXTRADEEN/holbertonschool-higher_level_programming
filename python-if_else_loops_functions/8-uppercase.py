#!/usr/bin/python3
def uppercase(str):
    ln = len(str)

    for i in range(ln):
        for str[i] >= 'a' and str[i] <= 'z':

            str[i] = chr(ord(str[i]) - 31)
