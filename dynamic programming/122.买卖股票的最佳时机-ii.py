#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 0 have stock, 1 don't have stock
        dp = [[0] * (2) for _ in range (len(prices))]
        dp[0][0] -= prices[0]
        for i in range(1, len(prices)):
           dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
           dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]

prices = [7,1,5,3,6,4]
print(Solution.maxProfit(Solution, prices))
# @lc code=end

