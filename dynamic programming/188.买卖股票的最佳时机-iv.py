#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp = [[0] * (k * 2) for _ in range (len(prices))]
        for j in range(0,len(dp[0]), 2):
            dp[0][j] -= prices[0]
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if j == 0:
                    dp[i][0] = max(dp[i - 1][0], - prices[i])
                elif j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        return dp[-1][-1]
# @lc code=end

