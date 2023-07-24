#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob1(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
    
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob1(nums[:len(nums) - 1]), self.rob1(nums[1:len(nums)]))

# @lc code=end

