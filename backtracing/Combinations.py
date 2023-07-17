class Solution:
    def combine(self, n: int, k: int):
        path = []
        result = []
        def backtracing(startIndex: int):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(startIndex,n + 1):
                if n + 1 - startIndex + len(path) < k:
                    return
                path.append(i)
                backtracing(i + 1)
                path.pop()
        backtracing(1)
        return result

n = 4
k = 2
print(Solution.combine(Solution,n,k))
        
        