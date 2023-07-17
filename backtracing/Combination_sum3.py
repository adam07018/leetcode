class Solution:
    def combinationSum3(self, k: int, n: int):
        ans = []
        path = []
        def backtracing(startIndex):
            sum = 0
            for i in path:
                sum += i
            if sum == n and len(path) == k:
                ans.append(path.copy())
                return
            # either number too big or too much number
            if sum > n or len(path) == k:
                return
            for i in range(startIndex, 10):
                path.append(i)
                backtracing(i + 1)
                path.pop()
        backtracing(1)
        return ans

k = 3
n = 9
print(Solution.combinationSum3(Solution,k,n))
