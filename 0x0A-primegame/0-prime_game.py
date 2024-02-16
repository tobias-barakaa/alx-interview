#!/usr/bin/python3
""" 
isWinner module
"""


def isWinner(x, nums):
    """
    Prime Game
    """
    if x < 1 or not nums:
        return None

    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    primes = [i for i, j in enumerate(primes) if j]

    m = 0
    for i in nums:
        while primes[m] < i:
            m += 1
        if primes[m] == i:
            m += 1
            x -= 1
            if x == 0:
                return "Maria"
        else:
            x -= 1
            if x == 0:
                return "Ben"
    return "Ben"

