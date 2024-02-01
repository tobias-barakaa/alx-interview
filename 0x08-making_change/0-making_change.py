#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Find the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any combination of coins.

    Raises:
        ValueError: If the input total is less than or equal to zero.

    Note:
        This function uses dynamic programming to optimize the solution.
    """
    if total <= 0:
        raise ValueError("Total amount must be greater than zero.")

    # Initialize a table to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the table using dynamic programming
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
