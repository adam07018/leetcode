#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j]
                if i == 0:
                    if j == 0:
                        continue
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

grid = [[1,2,3],[4,5,6]]
print(Solution.minPathSum(Solution,grid))
# @lc code=end

