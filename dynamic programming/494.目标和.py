#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        sum = 0
        for j in nums:
            sum += j
        if abs(target) > sum:
            return 0
        if (target + sum) % 2 == 1:
            return 0
        plus = (target + sum) // 2
        dp = [0] * (plus + 1)
        dp[0] = 1
        for i in nums:
            for j in range(plus, -1, -1):
                if  j >= i:
                    dp[j] += dp[j - i]
        return dp[-1]


    def findTargetSumWays1(self, nums: list[int], target: int) -> int:
        sum = 0
        for j in nums:
            sum += j
        if abs(target) > sum:
            return 0
        if (target + sum) % 2 == 1:
            return 0
        plus = (target + sum) // 2
        
        dp = [[0] * (plus + 1) for _ in range(len(nums))]

        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        for j in range(1, plus + 1):
            if j == nums[0]:
                dp[0][j] = 1

        for i in range(1,len(nums)):
            for j in range(plus+ 1):
                if j < nums[i]: # not enough weight
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 不放加上放
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
        
        return dp[-1][-1]

    def findTargetSumWays2(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)  # 计算nums的总和
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        target_sum = (target + total_sum) // 2  # 目标和

        # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化状态
        dp[0][0] = 1

        # 动态规划过程
        for i in range(1, len(nums) + 1):
            for j in range(target_sum + 1):
                dp[i][j] = dp[i - 1][j]  # 不选取当前元素
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选取当前元素

        return dp[len(nums)][target_sum]  # 返回达到目标和的方案数

nums = [0,0,0,0,0,0,0,0,1]
print(Solution.findTargetSumWays(Solution,nums,1))

# @lc code=end

