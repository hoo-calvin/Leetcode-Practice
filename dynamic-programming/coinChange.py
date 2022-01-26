"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money. Return the fewest number of coins 
that you need to make up that amount. If that amount of money cannot be made up by any combination 
of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""

def coinChange(coins, amount):
    # Edge cases
    if amount == 0 : return 0
    if len(coins) == 0: return 0
    # Create memo with amount+1 (we choose amt+1 cause it is not possible to reach this large 
    # number and we need to use min.)
    memo = [amount+1 for _ in range(amount + 1)]
    # Initialize 0 for 0.
    memo[0] = 0
    # Iterate through each index. Each index corresponds to each subvalue of amount.
    for index in range(1, amount + 1):
        # Go through each coin.
        for coin in coins:
            # Check if the math is valid.
            if index - coin >= 0:
                # The compare with mins with each coin calculation and adding a new coin from the prev possible.
                memo[index] = min(memo[index], 1 + memo[index-coin])
    # IF amount+1 is at the end. It wasnt possible to reach this value with the coins.
    if memo[amount] == amount+1:
        return -1
    else:
        return memo[amount]


if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
    print(coinChange([2], 3))
    print(coinChange([1], 0))