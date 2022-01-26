"""
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum 
amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        # Create a memo where each index represents the current max amount that can be robbed at each
        # house index.
        memo = [0 for _ in range(len(nums))]
        # Initialize the base cases.
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        # Using the base cases build up to the last house.
        for i in range(2, len(nums)):
            memo[i] = max(memo[i-2]+nums[i], memo[i-1])
        # Return the value of the last house.
        return memo[-1]
            