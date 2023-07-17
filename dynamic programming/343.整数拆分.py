#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        # 数组含义：biggest product of given index
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        # 递归顺序：from small to big
        # 递推公式：dp[i] 
        for i in range(4, n + 1):
            for j in range(1,4): # or range(1,i)
                dp[i] = max(dp[i],j * dp[i - j], j * (i - j))
        return dp[-1]

n = 20
print(Solution.integerBreak(Solution,n))
# @lc code=end

