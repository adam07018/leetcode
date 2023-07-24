#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # 先背包再物品
        for j in range(1, len(dp)):
            for i in wordDict:
                n = len(i)
                if j - n >= 0 and i == s[j - n:j] and dp[j - n]:
                    dp[j] = True
                    break
        return dp[-1]
                
s = 'leetcode'
wordDict = ["leet","code"]
print(Solution.wordBreak(Solution,s,wordDict))
# @lc code=end

