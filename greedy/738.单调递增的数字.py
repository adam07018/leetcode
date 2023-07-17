#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        s = list(s)
        # flag set to right index of number
        flag = len(s)
        # from right to left
        for i in range(len(s) - 1, 0, -1):
            if int(s[i - 1]) > int(s[i]):
                s[i - 1] = str(int(s[i - 1]) - 1 )
                s[i] = "9"
                flag = i
        for i in range(flag,len(s)):
            s[i] = "9"
        s = "".join(s)
        return int(s)

print(Solution.monotoneIncreasingDigits(Solution,332))
# @lc code=end

