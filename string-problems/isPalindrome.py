from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ""
        for char in s:
            if char.isalpha():
                word = word + char.lower()
        
        slow, fast = 0, 0
        queue = deque()
        while fast < len(word):
            curr = word[slow]
            queue.append(curr)
            slow += 1
            fast += 2
        
        fast = len(word)-1
        while fast >= slow:
            compareTo = queue.popleft()
            if word[fast] == compareTo:
                fast -= 1
            else:
                return False
        
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("race a car"))