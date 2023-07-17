# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets
# 链接：https://leetcode.cn/problems/3sum

from collections import Counter

class Solution:
    # 移动窗口双指针, 去重
    # Sort the array 
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            # 剪枝
            if nums[i] > 0: # only when target is >=0 can do this
                break
            # i不是指针，在while的时候不变
            # 所以i只能对照历史，不能用nums[i] == nums[i + 1]
            # eg. [-1,-1,2], if i = 0, nums[i] == nums[i + 1] is true, will return null
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                    continue
                if sum > 0:
                    right -= 1
                    continue
                # Result = 0, 去重
                ans.append([nums[i],nums[left],nums[right]])
                # 指针去重必须在while里面
                # eg. [0,0,0], 如果在外面去重，if left = 1, nums[left] == nums[left + 1], return null
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 去完重后还要移动指针
                left += 1
                right -= 1
        return ans
                
                
                