"""
Given an array of distinct integers nums and a target integer target, return the number of 
possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # We use a hash set to store the subvalues of num and 
        # the number of combinations to said subvalue.
        memo = {0 : 1}
        
        # check each subvalue up to target.
        for value in range(1, target + 1):
            # Initialize the value into the dictionary.
            memo[value] = 0
            # Check each num in nums.
            for num in nums:
                # if the value -nums is already in the memo. Add to current dict value.
                if value-num in memo:
                    memo[value] += memo[value-num]
        
        # Return the target combinations stored in memo.
        return memo[target]