#!/usr/bin/python3
"""
Prime Game to check the prime numbers
"""

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

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
    
    count = sum(1 for num in nums if is_prime(num))
    
    if count % 2 == 0:
        return "Ben"
    return "Maria"
