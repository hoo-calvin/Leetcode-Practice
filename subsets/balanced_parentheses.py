"""
For a given number 'N', write a function to generate all combination of 'N' pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

from collections import deque

class ParenthesesString:
    def __init__(self, string, openCount, closedCount):
        self.string = string
        self.openCount = openCount
        self.closedCount = closedCount

def find_all_balanced_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        curr = queue.popleft()
        if curr.openCount == num and curr.closedCount == num:
            result.append(curr.string)
        else:
            if curr.openCount < num:
                queue.append(ParenthesesString(curr.string+"(", curr.openCount+1, curr.closedCount))

            if curr.closedCount < curr.openCount:
                queue.append(ParenthesesString(curr.string+")", curr.openCount, curr.closedCount+1))
    
    return result

def main():
  print("All combinations of balanced parentheses are: " +
        str(find_all_balanced_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(find_all_balanced_parentheses(3)))


main()  