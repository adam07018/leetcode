#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_num = nums[0]
        for i in range(1,len(dp)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            if dp[i] > max_num:
                max_num = dp[i]
        return max_num
# @lc code=end

