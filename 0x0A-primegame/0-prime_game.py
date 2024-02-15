#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    
    Args:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
        str or None: Name of the player that won the most rounds, or None if winner cannot be determined.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_winner(round_nums):
        count = sum(1 for num in round_nums if is_prime(num))
        return "Maria" if count % 2 != 0 else "Ben"

    winners = [get_winner(nums[i]) for i in range(x)]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None