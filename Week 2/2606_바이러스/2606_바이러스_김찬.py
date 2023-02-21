from collections import deque

c = int(input())
graph = [[] for _ in range(c+1)]

n = int(input())
for i in range(n):
    # 양방향 간선 추가
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 이 문제에서는 정렬 불필요해보임
graph = [sorted(x) for x in graph]
visited = [0 for _ in range(c+1)]

def bfs(start):
    visited[start] = 1 # 시작노드 방문처리
    queue = deque([start])

    while queue:
        cur = queue.popleft() # 현재 노드
        for next in graph[cur]: # 이동 가능 노드
            if not visited[next]: # 방문하지 않았다면
                visited[next] = 1 # 방문 처리
                queue.append(next) # 큐에 추가

bfs(1)
print(visited.count(1)-1) # 1(방문처리)인 노드개수 - 1