# Given a string s containing only digits, return all possible valid IP addresses 
# that can be formed by inserting dots into s. 
# You are not allowed to reorder or remove any digits in s. 
# You may return the valid IP addresses in any order.
# https://leetcode.cn/problems/restore-ip-addresses
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        if n > 12 or n < 4:
            return []
        ans = []
        path = []
        def checkIP(s:str) -> bool:
            if len(s) > 1 and s[0] == '0':
                return False
            if int(s) > 255:
                return False
            return True
        def backtrace(startIndex):
            if len(path) == 4:
                if startIndex == n:
                    res = ''
                    for i in path:
                        res += i
                        res += "."
                    res = res[:len(res) - 1]
                    ans.append(res)
                return

            if startIndex + 3 > n:
                upperbound = n
            else:
                upperbound = startIndex + 3

            for i in range(startIndex, upperbound):
                temp = s[startIndex : i + 1]
                if not checkIP(temp):
                    break
                path.append(temp)
                backtrace(i + 1)
                path.pop()
        backtrace(0)
        return ans

s = "101023"
print(Solution.restoreIpAddresses(Solution, s))
