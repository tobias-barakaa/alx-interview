#!/usr/bin/python3
"""
Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, j in enumerate(primes) if j]
    wins = 0
    for n in nums:
        wins += sum(1 for i in primes if i <= n)
    return "Ben" if wins % 2 == 0 else "Maria"
