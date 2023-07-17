class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Every key of the original BST is changed to the original key 
# plus the sum of all keys greater than or equal to the original key in BST
class Solution:
    def convertBST(self, root:TreeNode):
        sum = 0
        def dfs(root):
            if root == None:
                return None
            nonlocal sum
            root.right = dfs(root.right)
            sum = sum + root.val
            root.val = sum
            root.left = dfs(root.left)
            return root
        return dfs(root)

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)
print(Solution.convertBST(Solution,root))