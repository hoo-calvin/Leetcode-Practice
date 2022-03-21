class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
    if not root: return None
    return dfs(root, 0)

def dfs(curr, pathSum):
    if not curr: return 0

    pathSum = (pathSum*10) + curr.val
    
    if not curr.left and not curr.right:
        return pathSum
    
    return dfs(curr.left, pathSum) + dfs(curr.right, pathSum)


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()