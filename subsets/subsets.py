"""
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

def find_subsets(nums):
    # Arr that holds all subsets which we return
    subsets = []
    # Append the first subset which is an empty arr.
    subsets.append([])
    # We add the current number to every current subset.
    for current in nums:
        curr_sub_len = len(subsets)
        # iterate through all the current subsets.
        for i in range(curr_sub_len):
            # Copy the current subset then append the current number 
            # and append to the list of subsets.
            new_set = subsets[i][::]
            new_set.append(current)
            subsets.append(new_set)

    return subsets

test = [1, 5, 3]
print(find_subsets(test))