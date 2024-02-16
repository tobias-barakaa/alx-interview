#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
    """ 
    Game Prime"""
    if nums is None or x < 1:
        return None
    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, j in enumerate(primes) if j]
    print(primes)
    return "Maria"
