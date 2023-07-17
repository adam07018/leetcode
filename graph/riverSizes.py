def riverSizes(matrix):
    # Write your code here.
    bitmap = [ [False] * len(matrix[0]) for i in range (len(matrix))]
    array = []
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if (bitmap[i][j] is True or matrix [i][j] == 0) :
                continue
            array.append(BFS(matrix, bitmap, i, j))
    return array

# Preasumption: value in matrix is 1
def DFS(matrix, bitmap, i, j):
    count = 1
    bitmap[i][j] = True
    # left 
    if (j - 1 >= 0 and matrix[i][j - 1] == 1 and bitmap[i][j - 1] is False):
        count += DFS(matrix, bitmap, i, j - 1)
    # right
    if (j + 1 < len(matrix[0]) and matrix[i][j + 1] == 1 and bitmap[i][j + 1] is False) :
        count += DFS(matrix, bitmap, i, j + 1)
    # up
    if (i - 1 >= 0 and matrix[i - 1][j] == 1 and bitmap[i - 1][j] is False) :
        count += DFS(matrix, bitmap, i - 1, j)
    # down
    if (i + 1 < len(matrix) and matrix[i + 1][j] == 1 and bitmap[i + 1][j] is False) :
        count += DFS(matrix, bitmap, i + 1, j)
    return count

from collections import deque
def BFS(matrix, bitmap, i, j):
    count = 0
    q = deque()
    tuple = (i, j)
    q.append(tuple)
    while (q):
        cur = q.popleft()
        i = cur[0]
        j = cur[1]
        count += 1
        bitmap[i][j] = True
        if (j - 1 >= 0 and matrix[i][j - 1] == 1 and bitmap[i][j - 1] is False):
            q.append((i, j - 1))
            bitmap[i][j - 1] = True
        if (j + 1 < len(matrix[0]) and matrix[i][j + 1] == 1 and bitmap[i][j + 1] is False) :
            q.append((i, j + 1))
            bitmap[i][j + 1 ] = True
        if (i - 1 >= 0 and matrix[i - 1][j] == 1 and bitmap[i - 1][j] is False) :
            q.append((i - 1, j))
            bitmap[i - 1][j] = True
        if (i + 1 < len(matrix) and matrix[i + 1][j] == 1 and bitmap[i + 1][j] is False) :
            q.append((i + 1, j))
            bitmap[i + 1][j] = True
    return count

matrix = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]]
riverSizes(matrix)