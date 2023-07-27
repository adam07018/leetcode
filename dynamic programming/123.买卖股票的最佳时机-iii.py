#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # dp[i][0] means first time holding stock
        dp = [[0] * (4) for _ in range (len(prices))]
        dp[0][0] -= prices[0]
        dp[0][2] -= prices[0]
        for i in range(1,len(dp)):
            dp[i][0] = max(dp[i - 1][0], - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
        return dp[-1][3]

# @lc code=end

