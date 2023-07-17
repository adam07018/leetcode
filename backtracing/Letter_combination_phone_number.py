class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        res = []
        path = ''
        def backtracing(path, digitIndex):
            if digitIndex == len(digits):
                res.append(path)
                return
            digit = digits[digitIndex]
            for i in range(0, len(map[digit])):
                path += map[digit][i]
                backtracing(path, digitIndex + 1)
                path = path[:-1]
        backtracing(path, 0)
        return res
    
digits = '23'
print(Solution.letterCombinations(Solution,digits))
                