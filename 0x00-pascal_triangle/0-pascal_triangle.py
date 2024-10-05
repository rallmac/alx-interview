#!/usr/bin/python3

"""
This function generates the pascal triangle
"""


def pascal_triangle(n):
    """ n represents the number of rows """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        """ Always call previous row if n is greater than 1 """
        prev_row = triangle[i - 1]

        """ Each row starts and ends with one """
        row = [1]

        """Generate the values of the pascal triangle"""

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
