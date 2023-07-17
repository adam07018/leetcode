#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        sum = 0
        for i in stones:
            sum += i
        target = int(sum / 2)
        dp = [0] * (target + 1)
        # 初始化
        for j in range(stones[0], len(dp)):
            dp[j] = stones[0]
        
        for i in range(1, len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        
        return sum - dp[-1] - dp[-1]


# @lc code=end

