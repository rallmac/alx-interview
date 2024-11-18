#!/usr/bin/python3
"""This Function rotates the 2d matrix by 90 degrees"""


def rotate_2d_matrix(matrix):
    """This prototype takes in input if the 2d matrix
    afterwards, it rotates without taking extra space
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
