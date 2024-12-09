#!/usr/bin/python3
"""This function determines the winner between two players
"""


def isWinner(x, nums):
    """The winner is determined after three rounds
    no card is left for the loosing player
    """
    if not nums or x < 1:
        return None

    # Precompute prime numbers using the Sieve of Eratosthenes
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each number
    primes_up_to = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_up_to[i] = primes_up_to[i - 1] + (1 if is_prime[i] else 0)

    # Simulate the game for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the total number of moves (number of primes up to n)
        total_moves = primes_up_to[n]
        # Maria starts, so if the total moves are odd, Maria wins
        # If even, Ben wins
        if total_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
