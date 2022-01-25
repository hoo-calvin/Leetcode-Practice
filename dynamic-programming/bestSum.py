"""
Write a function bestSum that takes a target number and an array of integers
as arguments.

The function should return an array containing the shortest combination of 
numbers that add up to exactly the target number.

(7, [5, 3, 4, 7]) => [7]
(8, [2, 3, 5]) => [3, 5]
"""



def bestSum_bruteForce(target, nums):

    # base cases for recursion.
    if target == 0: return []
    if target < 0: return None

    shortestComb = None

    for num in nums:
        remainder = target-num
        result = bestSum_bruteForce(remainder, nums)
        if result != None:
            newResult = result[:] + [num]
            if not shortestComb or (len(newResult) < len(shortestComb)):
                shortestComb = newResult
    
    return shortestComb

def bestSum_dp(target, nums, memo={}):

    # base cases for recursion.
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortestComb = None

    for num in nums:
        remainder = target-num
        result = bestSum_dp(remainder, nums, memo)
        if result != None:
            newResult = result[:] + [num]
            if not shortestComb or (len(newResult) < len(shortestComb)):
                shortestComb = newResult
    
    memo[target] = shortestComb
    return memo[target]

if __name__ == "__main__":
    print(bestSum_bruteForce(7, [5, 3, 4, 7]))
    print(bestSum_bruteForce(8, [2, 3, 5]))
    print(bestSum_bruteForce(8, [1, 4, 5])) 
    #print(bestSum_bruteForce(100, [1, 2, 5, 25])) # Takes too long.

    print(bestSum_dp(7, [5, 3, 4, 7]))
    print(bestSum_dp(8, [2, 3, 5]))
    print(bestSum_dp(8, [1, 4, 5])) 
    print(bestSum_dp(100, [1, 2, 5, 25])) # Takes too long.