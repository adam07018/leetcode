def cycleInGraph(edges):
    for i in range(len(edges)):
        visited = [False] * len(edges)
        if (dfs(edges, visited, i)):
            return True
    return False

# i is index of node want to dfs, j is index of verte of node to dfs
def dfs(edges, visited, i):
    if (visited[i]):
        return False   
    visited[i] = True
    if (len(edges[i]) == 0):
        return False
    for j in range(len(edges[i])):
        if (dfs(edges, visited, edges[i][j])):
            return True
    return False

edges = [
    [1, 2],
    [2],
    []]
print(cycleInGraph(edges))