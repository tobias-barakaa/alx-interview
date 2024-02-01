#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins: A list of coin denominations.
        total: The target amount to make change for.

    Returns:
        The minimum number of coins needed to make change, or -1 if it's not possible.
    """

    dp = [float('inf')] * (total + 1)  # Initialize a table to store minimum coin counts
    dp[0] = 0  # Base case: 0 coins needed to make 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Update minimum coins for each value

    return dp[total] if dp[total] != float('inf') else -1
