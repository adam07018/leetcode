# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        diff = pow(10,5) + 1
        pre = None
        def dfs(node):
            nonlocal diff
            nonlocal pre
            if not node:
                return
            dfs(node.left)
            if pre and abs(pre.val - node.val) < diff:
                diff = abs(pre.val - node.val)
            pre = node
            dfs(node.right)
        dfs(root)
        return diff