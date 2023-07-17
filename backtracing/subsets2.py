# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# https://leetcode.cn/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        path = []
        n = len(nums)
        nums.sort()
        def backtrace(startIndex):
            if startIndex == n:
                return
            for i in range(startIndex, n):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                ans.append(path.copy())
                backtrace(i + 1)
                path.pop()
            
        backtrace(0)
        return ans

nums = [1,2,2]
print(Solution.subsetsWithDup(Solution,nums))