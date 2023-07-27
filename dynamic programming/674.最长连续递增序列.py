#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max_num = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                if count > max_num:
                    max_num = count
                count = 1
        if count > max_num:
            max_num = count
        return max_num

num = [1,3,5,7]
Solution.findLengthOfLCIS(Solution, num)
# @lc code=end

