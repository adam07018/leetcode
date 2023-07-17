#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        dp = [-1] * len(cost)
        cost.append(0)
        dp.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]

cost = [10,15,20]
print(Solution.minCostClimbingStairs(Solution,cost))
 # @lc code=end

