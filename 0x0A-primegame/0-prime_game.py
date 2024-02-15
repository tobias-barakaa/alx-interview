#!/usr/bin/python3
"""
Prime Game"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    def get_winner(n):
        if n < 2:
            return None
        primes_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        return "Maria" if primes_count % 2 == 0 else "Ben"
    
    winner_count = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = get_winner(n)
        if winner:
            winner_count[winner] += 1
    
    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Maria"] < winner_count["Ben"]:
        return "Ben"
    else:
        return None
