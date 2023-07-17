#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum % 2 == 1:
            return False
        sum = int(sum / 2)
        bagweight = sum

        # 创造数组
        dp = [0] * (bagweight + 1)
        # 初始化
        for j in range(nums[0], bagweight + 1):
            dp[j] = nums[0]

        for i in range(1, len(nums)):
            for j in range(bagweight, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        # 遍历
        #for i in range(1, len(nums)):
            # j 是重量
            #for j in range(bagweight + 1):
                #if j >= nums[i]:
                    #dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
                #else:
                    #dp[i][j] = dp[i - 1][j]
        if dp[-1] == sum:
            return True
        return False

nums = [1,2,5]
print(Solution.canPartition(Solution,nums))
# @lc code=end

