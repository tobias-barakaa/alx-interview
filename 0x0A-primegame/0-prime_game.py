#!/usr/bin/python3
"""
Prime Game to check the prime numbers"""


def isWinner(x, nums):
  """
  Determines the winner of a prime number game played by Maria and Ben.

  Args:
    x: Number of rounds in the game.
    nums: List of consecutive integers representing the initial set.

  Returns:
    "Maria": If Maria wins the most rounds.
    "Ben": If Ben wins the most rounds.
    None: If the winner cannot be determined due to ties.
  """

  maria_wins = 0
  ben_wins = 0

  for _ in range(x):
    nums = _remove_multiples(nums)
    if not nums:
      break  # Game ends prematurely, Ben wins

    # Maria goes first, picks a prime and removes multiples
    prime_index = _find_prime_index(nums)
    prime = nums[prime_index]
    nums = _remove_multiples(nums, prime)

    if not nums:
      maria_wins += 1
      continue  # Maria wins this round

    # Ben goes second, picks a prime and removes multiples
    prime_index = _find_prime_index(nums)
    prime = nums[prime_index]
    nums = _remove_multiples(nums, prime)

    if not nums:
      ben_wins += 1
      continue  # Ben wins this round

    # Game continues to next round

  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None

def _remove_multiples(nums, prime=None):
  """
  Removes multiples of a given prime number from the list.

  Args:
    nums: List of integers.
    prime: Optional prime number to remove multiples of.

  Returns:
    List of integers with multiples removed.
  """

  return [num for num in nums if prime is None or num % prime != 0]

def _is_prime(num):
  """
  Checks if a number is prime.

  Args:
    num: Integer to check.

  Returns:
    True if prime, False otherwise.
  """

  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def _find_prime_index(nums):
  """
  Finds the index of the first prime number in the list.

  Args:
    nums: List of integers.

  Returns:
    Index of the first prime number, None if no prime found.
  """

  for i, num in enumerate(nums):
    if _is_prime(num):
      return i
  return None

# Example usage
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
