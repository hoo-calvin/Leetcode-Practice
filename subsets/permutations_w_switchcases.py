"""Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""

def find_perms(word):
    # Start with an array with the orginal string.
    permutations = []
    permutations.append(word)
    # Iterate through each index of the word.
    for i in range(len(word)):
        # If current index is a character. Numbers can be skipped.
        if word[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chars = list(permutations[j])
                chars[i]=chars[i].swapcase()
                permutations.append("".join(chars))

    return permutations

def main():
  print("String permutations are: " +
        str(find_perms("ad52")))
  print("String permutations are: " +
        str(find_perms("ab7c")))



main()