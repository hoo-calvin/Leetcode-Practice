"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.For example, [3,6,2,7] is a subsequence of 
the array [0,3,1,6,2,2,7].
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create a memo of size of nums and initialize with 1. 
        # 1 is the intial length of the subsequence
        memo = [1 for _ in range(len(nums))]
        # Store in variable that holds longest subsequence.
        longestSub = 1
        # Iterate from the back.
        for left in range(len(nums)-2, -1, -1):
            # Iterate every number after the current.
            for right in range(left+1, len(nums)):
                # Check if the condition for longest subsequence applies.
                if nums[left] < nums[right]:
                    # Check against each new max. (1+ because we are adding the current num.)
                    memo[left] = max(memo[left], 1+memo[right])
                    longestSub = max(longestSub, memo[left])
                    
        return longestSub