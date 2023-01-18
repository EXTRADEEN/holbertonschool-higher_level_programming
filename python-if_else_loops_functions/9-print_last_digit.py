#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ldigit = (-1) * number % 10
    else:
        ldigit = number % 10
    print(ldigit, end='')
    return(ldigit)
