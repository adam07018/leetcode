class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(isLeft, sum, node):
            if node.left:
                sum = dfs(True, sum, node.left)
            if node.right:
                sum = dfs(False, sum, node.right)
            if not node.left and not node.right and isLeft:
                return sum + node.val
            return sum
        return dfs(False,0,root)