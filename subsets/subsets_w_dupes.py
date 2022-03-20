"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:
Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
"""
def find_subsets_w_dupes(nums):
    subsets = []
    seen = set()
    subsets.append([])
    
    nums.sort()

    for curr_num in nums:
        sub_len = len(subsets)

        for i in range(sub_len):
            new = subsets[i][::]
            new.append(curr_num)
            if new not in subsets:
                subsets.append(new)

    
    return subsets

test =[1, 5, 3, 3]
print(find_subsets_w_dupes(test))