# https://leetcode.cn/problems/n-queens/
# https://www.bilibili.com/video/BV1Rd4y1c7Bq/?spm_id_from=333.788&vd_source=97e572d15b1ecc14453093c647491a4e

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        path = []
        invalidCol = {}

        def addQueen(j) -> str:
            str = ''
            for k in range(n):
                if k == j:
                    str += 'Q'
                else:
                    str += '.'
            return str    

        def checkDiagnol(i,j):
            # 左上
            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                if path[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            # 右上
            row = i - 1
            col = j + 1
            while row >= 0 and col < n:
                if path[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            return True

        def backtrace(row):
            if len(path) == n:
                ans.append(path.copy())
                return 
            for j in range(n):
                if (j in invalidCol and invalidCol[j] == 1) or not checkDiagnol(row, j):
                    continue
                path.append(addQueen(j))
                invalidCol[j] = 1
                backtrace(row + 1)
                path.pop()
                invalidCol[j] = 0

        backtrace(0)
        return ans

n = 5
print(Solution.solveNQueens(Solution,n))
                
