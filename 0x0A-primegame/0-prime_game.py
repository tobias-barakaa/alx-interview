#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
    """Prime Game to check the prime numbers"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if not primes[i]:
            continue
        for j in range(i*i, n + 1, i):
            primes[j] = False
    primes = [i for i, j in enumerate(primes) if j]
    primes = primes[1:]
    count = 0
    for i in nums:
        count += sum(j <= i for j in primes)
    if count % 2 == 0:
        return "Ben"
    return "Maria"
