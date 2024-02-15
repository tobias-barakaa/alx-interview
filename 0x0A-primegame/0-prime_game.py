#!/usr/bin/python3
"""
Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    def isPrime(n):
        """Prime Game"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_primes(n):
        """Prime Game"""
        primes = [0] * (n + 1)
        for i in range(1, n + 1):
            if isPrime(i):
                primes[i] = 1
        return primes

    def calculate_winner(primes):
        """Prime Game"""
        c = 0
        for i in range(len(primes)):
            if primes[i] == 1:
                c += 1
        if c % 2 == 0:
            return "Ben"
        return "Maria"

    primes = calculate_primes(max(nums))
    winner = calculate_winner(primes)
    return winner
