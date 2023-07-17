class Solution:
    def isSymmetric(self, root) -> bool:
        def check(left,right):
            if left == None or right == None:
                return left == right
            return left.val == right.val and check(left.left, right.right) and check(left.right,right.left)
        
        return check(root.left,root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left =TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(Solution.isSymmetric(Solution,root))