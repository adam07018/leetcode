def removeIslands(matrix):
    # Write your code here.
    bitmap = [ [False] * len(matrix[0]) for i in range (len(matrix))]
    for i in range (1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if (bitmap[i][j] is True or matrix[i][j] == 0) :
                continue
            toRemove = [ [False] * len(matrix[0]) for i in range (len(matrix))]
            if (dfs(matrix, bitmap, toRemove, i, j)):
                for m in range (1, len(matrix) - 1):
                    for n in range(1, len(matrix[0]) - 1):
                        if toRemove[m][n] is True:
                            matrix[m][n] = 0
    return matrix

def dfs(matrix, bitmap, toRemove, i, j):
    if (i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1) :
        isIsland = False
    else:
        isIsland = True
    toRemove[i][j] = True
    bitmap[i][j] = True
     # left 
    if (j - 1 >= 0 and matrix[i][j - 1] == 1 and bitmap[i][j - 1] is False):
        if(not dfs(matrix, bitmap, toRemove, i, j - 1)): # not an island
            isIsland = False
    if (j + 1 < len(matrix[0]) and matrix[i][j + 1] == 1 and bitmap[i][j + 1] is False) :
        if(not dfs(matrix, bitmap, toRemove, i, j + 1)):
            isIsland = False
    if (i - 1 >= 0 and matrix[i - 1][j] == 1 and bitmap[i - 1][j] is False) :
        if(not dfs(matrix, bitmap, toRemove, i - 1, j)):
            isIsland = False
    if (i + 1 < len(matrix) and matrix[i + 1][j] == 1 and bitmap[i + 1][j] is False) :
        if(not dfs(matrix, bitmap, toRemove, i + 1, j)):
            isIsland = False
    return isIsland