#!/usr/bin/python3
"""Module for making change problem
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed to
    meet a given amount total
    Args:
        coins: list of the values of the coins in your possession
        total: amount to be made with the coins
    Returns:
        Fewest number of coins needed to meet the total
    """
    if total <= 0:
        return 0

    """ Initialize a table to store the minimum number of
    coins for each amount
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the table using dynamic programming
    for coin in coins:
        if coin > total:
            continue
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
