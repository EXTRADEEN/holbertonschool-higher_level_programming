#!/usr/bin/python3
"""
    Module that creates a function: pascal_triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal's triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    
    for i in range(n):
        row = [1]
        for j in range(i + 1):
            if (j == 0) or (j == i):
                r = 1
            else:
                r = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(r)
        triangle.append(row)
    return triangle
