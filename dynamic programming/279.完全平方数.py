#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        square = [1]
        num = 2
        while pow(num, 2) <= n:
            square.append(pow(num, 2))
            num += 1
        for i in range(len(square)):
            for j in range(square[i], len(dp)):
                dp[j] = min(dp[j - square[i]] + 1, dp[j])
        return dp[-1]

print(Solution.numSquares(Solution,12))
# @lc code=end

