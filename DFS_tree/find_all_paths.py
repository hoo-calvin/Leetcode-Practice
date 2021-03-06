"""
Given a binary tree and a number "S", find all paths from root-to-leaf
such that the sum of all the node values of each path equals "S".
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths(root, targetSum):
    if not root: return []

    results = []
    dfs(root, targetSum, [], results)
    return results

def dfs(curr, target, currPath, results):
    if not curr: return None

    currPath.append(curr.val)

    if target - curr.val == 0 and not curr.left and not curr.right: 
        results.append(currPath[::])

    else:
        dfs(curr.left, target - curr.val, currPath, results)
        dfs(curr.right, target - curr.val, currPath, results)

    del currPath[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()