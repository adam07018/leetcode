class Solution:
    def isBalanced(self, root) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        if height(root) == -1:
            return False
        return True