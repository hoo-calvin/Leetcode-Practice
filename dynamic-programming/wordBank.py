"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    def wordBreak(self, s, wordDict, memo={}):
        # If the current word is already in the memo, just return it.
        if s in memo: return memo[s]
        # If the string is found to be empty, return True
        if s == "": return True
        
        # Check every word in the current wordDict.
        for word in wordDict:
            # Get the len of the current word and use it to get the current prefix of the word.
            wordLen = len(word)
            prefix = s[:wordLen]
            # Check if the prefix is in the wordbank.
            if prefix in wordDict:
                # Remove the prefix to check for the next word.
                newWord = s[wordLen:]
                # If the next word returns true. Then add the current word s to the memo.
                if self.wordBreak(newWord, wordDict, memo):
                    memo[s] = True
                    return True
        
        # Everything failed so return False.
        memo[s] = False
        return False


if __name__ == "__main__":
    s = Solution()
    word = "catsandog"
    wordBank = ["cats","dog","sand","and","cat"]

    word = "a"
    wordBank = ["b"]

    print(s.wordBreak(word, wordBank)) # False