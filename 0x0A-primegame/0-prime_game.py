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

    def calculate_primes(n):
        primes = [True for i in range(n + 1)]
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i, prime in enumerate(primes) if prime][1:]

    def play_game(n, primes):
        count = 0
        for i in range(n):
            if i in primes:
                count += 1
        return count % 2 == 0

    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        primes = calculate_primes(n)
        if play_game(n, primes):
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
