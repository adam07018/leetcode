#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp = [[0] * (2) for _ in range (len(prices))]
        dp[0][0] -= prices[0]
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return dp[-1][1]
# @lc code=end

