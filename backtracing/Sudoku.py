class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        n = len(board)

        def isValid(row, col, val:str) -> bool:
            # check row
            for j in range(n):
                if board[row][j] == val:
                    return False
            # check col
            for i in range(n):
                if board[i][col] == val:
                    return False
            # check square
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == val:
                        return False
            return True


        def backtrace(board) -> bool:
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if not isValid(i,j,str(k)):
                                continue
                            board[i][j] = str(k)
                            if backtrace(board):
                                return True
                            board[i][j] = '.'
                        # After try one place from one to nine still can't fit, so unsolvable
                        return False
            # everywhere is filled, sudoku solved
            return True

        backtrace(board)
        return board

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution.solveSudoku(Solution,board))
