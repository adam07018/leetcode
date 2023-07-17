# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# https://leetcode.cn/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []
        sum = 0
        n = len(candidates)
        def backtracing(startIndex,sum):
            if sum == target:
                ans.append(path.copy())
                return
            if sum > target:
                return
            for i in range(startIndex, n):
                element = candidates[i]
                path.append(element)
                sum += element
                backtracing(i, sum)
                path.pop()
                sum -= element
        backtracing(0,sum)
        return ans

candidates = [2,3,6,7]
target = 7
print (Solution.combinationSum(Solution,candidates,target))