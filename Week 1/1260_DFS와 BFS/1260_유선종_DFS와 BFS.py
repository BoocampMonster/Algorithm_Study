import sys

input = lambda: sys.stdin.readline().strip()

N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]

for _ in range(M):
    parrent, child = map(int, input().split())
    node[parrent].append(child)
    node[child].append(parrent)

node = [sorted(n) for n in node]
visited = [False] * (N+1)
dfs_result = [V]
def dfs(i):
    visited[i] = True
    for n in node[i]:
        if not visited[n]:
            dfs_result.append(n)
            dfs(n)
dfs(V)

visited = [False] * (N+1)
bfs_list = [V]
bfs_result = [V]
while bfs_list:
    root = bfs_list.pop(0)
    visited[root] = True
    for n in node[root]:
        if not visited[n]:
            bfs_result.append(n)
            bfs_list.append(n)
            visited[n] = True
print(*dfs_result)
print(*bfs_result)