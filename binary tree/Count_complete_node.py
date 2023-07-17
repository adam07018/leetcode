# Given the root of a complete binary tree, return the number of the nodes in the tree
# https://leetcode.cn/problems/count-complete-tree-nodes

class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        def isfulltree(root):
            left = root.left
            right = root.right
            depth = 1
            while left and right:
                left = left.left
                right = right.right
                depth += 1
            if left != right:
                return -1
            return depth
        depth = isfulltree(root)
        if depth == -1:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return pow(2, depth) - 1