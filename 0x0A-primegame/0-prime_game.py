#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        prime_count = sum(1 for num in range(2, n + 1) if is_prime(num))
        
        return "Ben" if prime_count % 2 == 0 else "Maria"

    winners = [calculate_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
