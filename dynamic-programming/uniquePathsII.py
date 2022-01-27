"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Ex.)
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rowSize = len(obstacleGrid)
        colSize = len(obstacleGrid[0])
        # Initialize a (m+1) by (n+1) grid
        dp = [[0 for _ in range(colSize+1)] for _ in range(rowSize + 1)]
        # Starting from the goal we set that index to 0.
        dp[rowSize - 1][colSize - 1] = 1
        # Iterate through each row.
        for row in range(rowSize-1, -1, -1):
            # Iterate from each column. Ignoring the dummy row and cols
            for col in range(colSize-1, -1, -1):
                # If the current square is an obstacle. We set its possibility to 0
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                # Possibility is calcuated by getting the right and bottom values.
                else:
                    dp[row][col] += dp[row+1][col] + dp[row][col+1]

        # Return the possiblities to get to the beginning of the obstacle grid.
        return dp[0][0]