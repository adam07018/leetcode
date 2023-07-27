#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        rows = len(triangle)
        dp = [[float('inf')] * (i + 1) for i in range(rows)]
        for i in range(rows):
            for j in 
# @lc code=end

