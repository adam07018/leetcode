#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        # 数组含义：dp[n] : number of BSTs with n nodes
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # 遍历顺序：BSTs with 1 node to BSTs with n nodes
        for i in range(2,n + 1):
            # 递推公式：root node start from smallest to largetst. eg. 1 to n
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[-1]
            

print(Solution.numTrees(Solution,3))
# @lc code=end

