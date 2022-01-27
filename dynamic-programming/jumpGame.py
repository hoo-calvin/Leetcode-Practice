"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Create dp of same len as nums 1:1
        dp = [0 for _ in range(len(nums))]
        # Initalize the base of the dp.
        dp[0] = nums[0]
        # Iterate through the dp while checking prev index.
        for i in range(1, len(nums)):
            # If the prev index cant reach the current. Return false.
            if dp[i-1] < i:
                return False
            # We store the furthest index we can reach from this point.
            dp[i] = max(i+nums[i], dp[i-1])
        # Dp has been filled and we check if the the furthest index 
        # the goal can reach is itself. If not we return false.
        if dp[-1] < len(nums)-1:
            return False
        else:
            return True