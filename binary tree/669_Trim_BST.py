class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root:TreeNode, low: int, high: int):
        if root == None:
            return None
        if root.val > high:
            return self.trimBST(Solution,root.left,low,high)
        if root.val < low:
            return self.trimBST(Solution,root.right,low,high)
        root.left = self.trimBST(Solution,root.left,low,high)
        root.right = self.trimBST(Solution,root.right,low,high)
        return root

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
low = 1
high = 3
print(Solution.trimBST(Solution,root,low,high).val)