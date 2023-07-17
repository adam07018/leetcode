class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = len(g) - 1
        j = len(s) - 1
        res = 0
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                res += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return res