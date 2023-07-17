#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]
        if n <= 2:
            return dp[n - 1]
        while n > len(dp):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
        
# @lc code=end

