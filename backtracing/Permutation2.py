# input with duplication
# Input: nums = [1,1,2]
# Output:[[1,1,2],[1,2,1],[2,1,1]]

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        # 树枝
        used = {}
        n = len(nums)
        def backtrace():
            if len(path) == n:
                ans.append(path.copy())
                return
            # 树层
            visited = {}
            for i in range(n):
                # 树枝去重，只看index不看value
                if i in used and used[i] == 1:
                    continue
                cur = nums[i]
                # 树层去重，只看value
                if cur in visited and visited[cur] == 1:
                    continue
                path.append(cur)
                visited[cur] = 1
                used[i] = 1
                backtrace()
                path.pop()
                # 树枝回溯
                used[i] = 0
        backtrace()
        return ans

nums = [1,1,2]
print(Solution.permuteUnique(Solution,nums))