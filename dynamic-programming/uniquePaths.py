"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to 
reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
Input: m = 3, n = 7
Output: 28
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 0 or m == 0:
            return 1
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = 1
        print(dp)
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                dp[row][col] += dp[row+1][col] 
                dp[row][col] += dp[row][col+1]
        
        return dp[0][0]

s = Solution()
print(s.uniquePaths(3, 2))