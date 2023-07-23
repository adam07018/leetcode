#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], len(dp)):
                #r = j % coins[i]
                #q = (j - r) // coins[i]
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

coins = [2]
amount = 3
print(Solution.coinChange(Solution,coins,amount))
            
# @lc code=end

