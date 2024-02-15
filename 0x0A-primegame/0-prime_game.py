#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
    """Prime Game
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
    primes_wins = 0
    for i in nums:
        primes_in_game = 0
        for j in primes:
            if j > i:
                break
            primes_in_game += 1
        if primes_in_game % 2 == 0:
            primes_wins += 1
    if primes_wins * 2 == len(nums):
        return None
    if primes_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
