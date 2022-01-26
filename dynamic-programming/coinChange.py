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

# def generateCoins(coins, amount, memo={}):
#     if amount in memo: return memo[amount]
#     if amount == 0: return []
#     if amount < 0: return None

#     smallestComb = None
    
#     for coin in coins:
#         remaining = amount - coin
#         result = generateCoins(coins, remaining, memo)
#         if result is not None:
#             newComb = result[:] + [coin]
#             if smallestComb is None or len(smallestComb) > len(newComb):
#                 smallestComb = newComb
    
#     memo[amount] = smallestComb
#     return memo[amount]

# def coinChange(coins, amount):
    
#     if amount == 0: return 0

#     result = generateCoins(coins, amount)
#     print(result)
#     if sum(result) != amount:
#         return -1
#     else:
#         return len(result)

def coinChange(coins, amount):
    
    if amount == 0: return 0
    
    def helper(coins, amount):
        if amount == 0: return 1
        if amount < 0: return 0

        totalWays = 0

        for coin in coins:
            remainder = amount-coin
            if remainder >= 0:
                totalWays += helper(coins, amount)

        return totalWays

    return helper(coins, amount)            


if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
    print(coinChange([2], 3))
    print(coinChange([1], 0))