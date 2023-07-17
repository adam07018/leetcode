# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Input: candidates = [10,1,2,7,6,1,5], target = 8

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path =[]
        n = len(candidates)
        candidates.sort()
        #visited = [False] * n
        sum = 0
        def backtrace(startIndex, sum):
            if sum == target:
                ans.append(path.copy())
                return
            if sum > target:
                return
            for i in range(startIndex, n):
                # 树层去重
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                sum += candidates[i]
                #visited[i] = True
                backtrace(i + 1, sum)
                path.pop()
                sum -= candidates[i]
                #visited[i] = False
        backtrace(0,sum)
        return ans

candidates = [2,5,2,1,2]
target = 5
print(Solution.combinationSum2(Solution, candidates, target))
