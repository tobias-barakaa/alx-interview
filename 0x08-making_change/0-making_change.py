#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[total] == total + 1 else dp[total]
