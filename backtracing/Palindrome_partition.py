# Given a string s, partition s such that every substring of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.
# https://leetcode.cn/problems/palindrome-partitioning
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

class Solution:
    # 切割而不是一个个选
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        def isPalindrome(s:str) -> bool:
            begin = 0
            end = len(s) - 1
            while (begin < end):
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True
        def backtrace(startIndex):
            if startIndex == len(s):
                ans.append(path.copy())
                return
            for i in range(startIndex,len(s)):
                temp = s[startIndex : i + 1]
                if not isPalindrome(temp):
                    continue
                path.append(temp)
                backtrace(i + 1)
                path.pop()
        backtrace(0)
        return ans
            
s = 'a'
print(Solution.partition(Solution, s))