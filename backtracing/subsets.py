# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# https://leetcode.cn/problems/subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        path = []
        n = len(nums)
        def backtrace(startIndex):
            if startIndex == n:
                return
            for i in range(startIndex, n):
                path.append(nums[i])
                ans.append(path.copy())
                backtrace(i + 1)
                path.pop()
            
        backtrace(0)
        return ans

nums = [1,2,3]
print(Solution.subsets(Solution,nums))