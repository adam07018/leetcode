#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        Dict = {}
        for i in range(len(s) - 1,-1,-1):
            if s[i] not in Dict:
                Dict[s[i]] = i
        ans = []
        bound = Dict.get(s[0])
        num = 0
        for i in range(len(s)):
            num += 1
            bound = max(bound,Dict.get(s[i]))
            if i == bound:
                ans.append(num)
                num = 0
        return ans

s = "eaaaabaaec"
print(Solution.partitionLabels(Solution,s))
        

# @lc code=end

