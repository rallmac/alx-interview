#!/usr/bin/python3
"""
This module contains the minOperations function.
"""


def minOperations(n):
    """Calculates the fewest number of operations to
       get n 'H' characters
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
