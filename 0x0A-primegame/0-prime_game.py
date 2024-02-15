#!/usr/bin/python3
"""
Prime Game"""


def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def find_next_prime(start, nums):
        for num in range(start, max(nums) + 1):
            if is_prime(num) and num in nums:
                return num
        return None

    wins = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        turn = 'Maria'
        current_nums = list(range(1, nums[i] + 1))

        while True:
            prime = find_next_prime(2, current_nums)
            if prime is None:
                break
            current_nums = [num for num in current_nums if num % prime != 0]
            turn = 'Ben' if turn == 'Maria' else 'Maria'

        if turn == 'Maria':
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1

    if wins['Maria'] == wins['Ben']:
        return None
    return max(wins, key=wins.get)
