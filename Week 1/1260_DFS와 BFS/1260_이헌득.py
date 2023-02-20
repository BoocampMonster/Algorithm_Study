n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x,y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def dfs(start, visited):
    visited.append(start)
    for idx in range(1, len(matrix[start])):
        if matrix[start][idx] == 1 and (idx not in visited):
            dfs(idx, visited)
    return visited    

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for idx in range(1, len(matrix[start])):
            if matrix[n][idx] == 1 and (idx not in visited):
                visited.append(idx)
                queue.append(idx)
    return visited

print(*dfs(v,[]))
print(*bfs(v))