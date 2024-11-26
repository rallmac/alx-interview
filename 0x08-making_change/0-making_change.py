#!/usr/bin/python3
"""This function determines a the number of coins needed to
   meet a given amount
"""


def makeChange(coins, total):
    """This module determines the fewest number of coins"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

        if dp[total] != float('inf'):
            break

    return dp[total] if dp[total] != float('inf') else -1
