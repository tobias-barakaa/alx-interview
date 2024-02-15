#!/usr/bin/python3
"""
Prime Game to check the prime numbers
"""


def generate_primes(n):
    """Generate prime numbers up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, prime in enumerate(primes) if prime][1:]


def isWinner(x, nums, primes):
    """Prime Game to check the prime numbers
    Args:
        x: the number of rounds
        nums: the list of numbers
        primes: list of pre-calculated prime numbers
    Returns:
        the winner of the game
    """
    if nums is None or x < 1:
        return None
    count = sum(1 for i in nums if i in primes)
    return "Ben" if count % 2 == 0 else "Maria"
