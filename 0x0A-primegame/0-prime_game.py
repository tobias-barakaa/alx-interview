#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
    """Prime Game to check the prime numbers
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, j in enumerate(primes) if j]
    p1 = 0
    for i in nums:
        p1 += sum([1 for j in primes if j <= i])
    if p1 % 2 == 0:
        return "Ben"
    return "Maria"