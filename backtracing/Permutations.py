# input without duplication
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        visited = {}
        n = len(nums)
        def backtrace():
            if len(path) == n:
                ans.append(path.copy())
                return 
            for i in nums:
                if i in visited and visited[i] == 1:
                    continue
                path.append(i)
                visited[i] = 1
                backtrace()
                path.pop()
                visited[i] = 0
        backtrace()
        return ans

nums = [1,2,3]
print(Solution.permute(Solution, nums))