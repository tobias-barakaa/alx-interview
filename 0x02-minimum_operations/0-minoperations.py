#!/usr/bin/python3
"""
minimum operations
"""

def minOperations(n):
    """
    Calculate the minimum
    number of operations required to achieve 'n' characters in a file.

    Parameters:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while i * i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    if n > 1:
        operations += n

    return operations
