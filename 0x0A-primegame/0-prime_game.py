#!/usr/bin/python3
""" 
    Prime Game"""
    

def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i in range(n + 1) if sieve[i]]
    m = len(sieve)
    dp = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        dp[i] = dp[i + 1]
        if sieve[i] in nums:
            dp[i] += 1
    if dp[0] == 0:
        return None
    if dp[0] % 2 == 0:
        return "Ben"
    return "Maria"
