#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp means number of paths to reach this point
        dp = [[0 for j in range(n)] for i in range(m)]
        # first row is 1
        for j in range(n):
            dp[0][j] = 1
        # first col is 1
        for i in range(m):
            dp[i][0] = 1
        # iterate from left to right, top to bottom
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
# @lc code=end

