#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root:TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, root: TreeNode) -> list[int]:
        if not root:
            return [0,0]
        leftdp = self.dfs(root.left)
        rightdp = self.dfs(root.right)
        value0 = max(leftdp[0], leftdp[1]) + max(rightdp[0],rightdp[1])
        value1 = root.val + leftdp[0] + rightdp[0]
        return [value0,value1] 
        
        
# @lc code=end

