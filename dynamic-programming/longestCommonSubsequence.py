"""
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) 
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

# Note: we work our way backwards from a 2x2 matrix. 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize a 2x2 matrix of length text1 and width text2
        memo = [[0 for col in range(len(text2)+1)] for row in range(len(text1) + 1)]
        # Iterate through each row. 
        for row in range(len(text1)-1, -1, -1):
            # Iterate through each column.
            for col in range(len(text2)-1, -1, -1):
                # if the current letter for text1 and text2 match. Add 1 to the value directly to its diagonal.
                if text1[row] == text2[col]:
                    memo[row][col] = 1 + memo[row+1][col+1]
                # if they dont match, we grab the greater of its right or bottom value.
                else:
                    memo[row][col] = max(memo[row+1][col], memo[row][col+1])
        
        # The length of the longest common subsequence is stored in the 1st row and column.
        return memo[0][0]