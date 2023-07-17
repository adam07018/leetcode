from collections import deque
def minimumPassesOfMatrix(matrix):
    q = deque()
    oneRound = True
    time = 0
    target = (-1, -1)
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if matrix[i][j] > 0:
                q.append((i,j))
    while q:
        cur = q.popleft()
        i = cur[0]
        j = cur[1]
        if cur == target:
            time += 1
            oneRound = True
        # top
        if (i > 0 and matrix[i - 1][j] < 0):
            matrix[i - 1][j] *= -1
            q.append((i-1,j))
            if oneRound:
                target = (i-1,j)
                oneRound = False
        # right
        if (j < len(matrix[0]) - 1 and matrix[i][j + 1] < 0):
            matrix[i][j + 1] *= -1
            q.append((i,j + 1))
            if oneRound:
                target = (i,j + 1)
                oneRound = False
        # bottom
        if (i < len(matrix) - 1 and matrix[i + 1][j] < 0):
            matrix[i + 1][j] *= -1
            q.append((i + 1, j))
            if oneRound:
                target = (i + 1,j)
                oneRound = False
        # left
        if (j > 0 and matrix[i][j - 1] < 0):
            matrix[i][j - 1] *= -1
            q.append((i, j - 1))
            if oneRound:
                target = (i,j - 1)
                oneRound = False
    
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if matrix[i][j] < 0:
                return -1
    return time

matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
  ]
print(minimumPassesOfMatrix(matrix))