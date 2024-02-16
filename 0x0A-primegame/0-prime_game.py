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
    primes = [True for _ in range(n + 1)]
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, j in enumerate(primes) if j]
    primes = primes[1:]
    count = 0
    for i in nums:
        if i in primes:
            count += 1
    if count % 2 == 0:
        return "Ben"
    return "Maria"

