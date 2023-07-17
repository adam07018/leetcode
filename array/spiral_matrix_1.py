def spiralTraverse(array):
    m = len(array)
    n = len(array[0])
    answer = []
    startRow, startCol, endRow, endCol = 0,0,m - 1,n - 1
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol, 1):
            answer.append(array[startRow][col])

        for row in range(startRow, endRow, 1):
            answer.append(array[row][endCol])

        for col in range(endCol, startCol, -1):
            if startRow == endRow:
                break
            answer.append(array[endRow][col])

        for row in range(endRow, startRow, -1):
            if startCol == endCol:
                break
            answer.append(array[row][startCol])
        startRow+=1
        endRow -= 1
        startCol +=1
        endCol-=1
    if m % 2 == 1 or n % 2 == 1:
        answer.append(array[startRow][startCol])
    
    return answer

array = [
    [1,2,3,4,5],
    [20,21,22,23,6],
    [19,32,33,24,7],
    [18,31,34,25,8],
    [17,30,35,26,9],
    [16,29,28,27,10],
    [15,14,13,12,11]
  ]

print(spiralTraverse(array))
            