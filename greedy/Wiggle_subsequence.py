# A wiggle sequence is a sequence where the differences between successive numbers 
# strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. 
# A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
# Given an integer array nums, return the length of the longest wiggle subsequence of nums
# https://leetcode.cn/problems/wiggle-subsequence

class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        result = 1
        if len(nums) == 1:
            return result
        prediff = 0
        curdiff = 0
        for i in range(len(nums) - 1):
            curdiff = nums[i + 1] - nums[i]
            if (prediff >= 0 and curdiff < 0) or (prediff <= 0 and curdiff > 0):
                result += 1
                prediff = curdiff
        return result
    