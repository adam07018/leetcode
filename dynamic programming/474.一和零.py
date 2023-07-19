#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = dp = [[0] * (n + 1) for _ in range(m  + 1)]
        for s in strs:
            zeroNum = s.count("0")
            oneNum = s.count("1")
            for i in range(m,zeroNum - 1,-1):
                for j in range(n, oneNum - 1,-1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)
        return dp[-1][-1]

strs = ["10","0001","111001","1","0"]
print(Solution.findMaxForm(Solution,strs,5,3))
# @lc code=end

