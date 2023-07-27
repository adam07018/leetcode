#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        # 横轴为nums1， 竖轴为nums2
        dp = [[0] * len(nums1) for _ in range(len(nums2))]
        max = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == nums2[i]:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max:
                        max = dp[i][j]
        return max

nums1 = [0,0,0,0,1]
nums2 = [1,0,0,0,0]
Solution.findLength(Solution, nums1, nums2)

# @lc code=end

