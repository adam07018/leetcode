#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, target + 1):
            for i in nums:
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[-1]

# @lc code=end

