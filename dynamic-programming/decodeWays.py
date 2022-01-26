"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using 
the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # Initialize the base case. An empty string contains only one way.
        dp = {len(s): 1}
        
        def dfs(i):
            # Basecase 1: We've seen this before or it is end of the string.
            if i in dp: 
                return dp[i]
            # Basecase 2: The string starts with zero.
            if s[i] == "0":
                return 0
            
            # Not zero is between 1-9. Can be taken as a single digit.
            res = dfs(i+1)
            
            # Handle cases where the 2 digits are valid.10-26
            if (i+1 < len(s)) and (s[i]== "1" or (s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i]=res
            return res
        
        return dfs(0)