def isWinner(x, nums):
   """
   Determines the winner of a prime number game played by Maria and Ben.

   Args:
       x: Number of rounds in the game.
       nums: List of consecutive integers representing the initial set.

   Returns:
       "Maria": If Maria wins the most rounds.
       "Ben": If Ben wins the most rounds.
       None: If the winner cannot be determined.
   """

   if nums is None or x < 1:
       return None

   maria_wins = 0
   ben_wins = 0

   for _ in range(x):
       # Generate primes up to the maximum number in the current round
       n = max(nums)
       primes = [True] * (n + 1)
       primes[0] = primes[1] = False
       for i in range(2, int(n**0.5) + 1):
           if primes[i]:
               for j in range(i * i, n + 1, i):
                   primes[j] = False
       primes = [i for i, prime in enumerate(primes) if prime]

       # Simulate the game for the current round
       while nums:
           prime_index = next((i for i, num in enumerate(nums) if num in primes), None)
           if prime_index is None:
               break  # No primes left, Ben wins this round

           prime = nums[prime_index]
           nums = [num for num in nums if num % prime != 0]

           if not nums:
               if maria_wins == ben_wins:
                   maria_wins += 1  # Maria wins the round if it's tied before this move
               break

           # Ben's turn (same logic as Maria's turn)
           prime_index = next((i for i, num in enumerate(nums) if num in primes), None)
           if prime_index is None:
               break  # No primes left, Maria wins this round

           prime = nums[prime_index]
           nums = [num for num in nums if num % prime != 0]

           if not nums:
               ben_wins += 1
               break

   if maria_wins > ben_wins:
       return "Maria"
   elif ben_wins > maria_wins:
       return "Ben"
   else:
       return None
