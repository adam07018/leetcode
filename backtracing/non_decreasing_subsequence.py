# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array
# with at least two elements. You may return the answer in any order.
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# https://leetcode.cn/problems/non-decreasing-subsequences
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)
        def backtrace(startIndex):
            if len (path) >= 2:
                ans.append(path.copy())
            visited = {}
            for i in range(startIndex,n):
                cur = nums[i]
                # check if it is decreasing
                if len(path) >= 1 and cur < path[len(path) - 1]:
                    continue
                if cur in visited:
                    continue
                path.append(nums[i])
                visited[cur] = 1
                backtrace(i + 1)
                path.pop()
        backtrace(0)
        return ans

nums = [4,6,7,7]
print(Solution.findSubsequences(Solution,nums))
                
                