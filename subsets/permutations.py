"""
Given a set of distinct numbers, find all of its permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""

from collections import deque

def find_permutations(nums):
    numsLength = len(nums)
    results = []
    # use a deque with an empty list to deal with permutations.
    permutations = deque([[]])
    print(permutations)
    # First loop to iterate through each number.
    for currNum in nums:
        # Second loop to iterate through each current permutation.
        n = len(permutations)
        for _ in range(n):
            # Third loop adds the current number to each index of each permutation.
            oldPerm = permutations.popleft()
            for j in range(len(oldPerm) + 1):
                # Copy the current perm
                newPerm = oldPerm[::]
                # Add the new number to specific index
                newPerm.insert(j, currNum)
                # Append to permutation if len is same as original str.
                if len(newPerm) == numsLength: 
                    results.append(newPerm)
                # Add back to permutations array if not complete.
                else:
                    permutations.append(newPerm)
    # Return the results.
    return results

test = [1, 3, 5]
print(find_permutations(test))