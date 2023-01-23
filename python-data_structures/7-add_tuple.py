#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b < 2:
        tuple_a = tuple_a (0, 0)
    if tuple_a and tuple_b > 2:
        tupple_a = tuple_a [2:]
    return(tuple(map(sum, zip(a, b))))
