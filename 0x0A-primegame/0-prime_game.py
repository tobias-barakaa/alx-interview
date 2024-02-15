#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Prime Game
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] is True:
            for j in range(i ** 2, n + 1, i):
                primes[j] = False

    primes = [i for i, j in enumerate(primes) if j is True]

    count = 0
    for i in nums:
        if i in primes:
            count += 1

    return "Ben" if count % 2 == 0 else "Maria"