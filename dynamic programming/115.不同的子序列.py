#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(1,len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

s = 'b'
t = 'b'
Solution.numDistinct(Solution, s, t)
# @lc code=end

