#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root:TreeNode) -> int:
        # 0 no camera cover, 1 camera install, 2 no camera but covered
        count = 0

        def dfs(node:TreeNode) -> int:
            # empty node return 2 so leaf node no camera
            nonlocal count
            if not node:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)
            # install camera when left or right child is not covered
            if left == 0 or right == 0:
                count += 1
                return 1
            # when there is a camera in left or right child
            if left == 1 or right == 1:
                return 2
            # no camera in child
            return 0
        
        if dfs(root) == 0:
            count += 1
        return count


# @lc code=end

