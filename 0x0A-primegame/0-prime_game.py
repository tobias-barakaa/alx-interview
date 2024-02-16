#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
    """Prime Game to check the prime numbers
    Args:
        x: the number of rounds
        nums: the list of numbers
    Returns:
        the winner of the game
    """
    if nums is None or x < 1:
        return None
    n = max(nums)
    primes = [True for i in range(n + 1)]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, prime in enumerate(primes) if prime]
    primes = primes[1:]
    count = 0
    for i in nums:
        if i in primes:
            count += 1
    if count % 2 == 0:
        return "Ben"
    return "Maria"