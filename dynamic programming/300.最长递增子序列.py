#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        maxnum = 1
        dp = [1] * len(nums)
        for i in range(len(dp)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > maxnum:
                        maxnum = dp[i]
        return maxnum

nums = [10,9,2,5,3,7,101,18]
print(Solution.lengthOfLIS(Solution,nums))
# @lc code=end

