from collections import deque
n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    # 양방향 간선이므로 둘 다 그래프에 추가
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# 여러 개 방문 가능시 작은 것부터 방문하도록 정렬
for i in range(1,len(graph)):
    graph[i].sort()

# 0부터 n까지 False처리하여 번호를 인덱스로 바로 사용
visited = [False for _ in range(n+1)]
visited[v] = True # 시작점
dfs = [v] # 시작점

def DFS(start):
    # 현 노드에서 방문할 수 있는 모든 노드에 대해
    for node in graph[start]:
        # 아직 방문하지 않은 경우에만
        if not visited[node]:
            visited[node] = True # 방문 처리
            dfs.append(node) # 방문 순서 기록
            DFS(node) # 새 노드를 기준으로 다시 탐색
DFS(v)

# 0부터 n까지 False처리하여 번호를 인덱스로 바로 사용
visited = [False for _ in range(n+1)]
visited[v] = True # 시작점
bfs = [v] # 시작점

def BFS(start):
    queue = deque([start]) # 시작점
    
    while queue: # 큐에 원소가 남아있는 동안 반복
        now = queue.popleft() # 가장 왼쪽 원소 꺼내기
        # 현 노드에서 방문할 수 있는 모든 노드에 대해
        for node in graph[now]:
            # 아직 방문하지 않은 경우에만
            if not visited[node]:
                visited[node] = True # 방문 처리
                queue.append(node) # 큐에 추가
                bfs.append(node) # 방문 순서 기록
BFS(v)

print(*dfs,sep=' ') # 리스트 모든 원소를 공백으로 구분하여 출력
print(*bfs,sep=' ')
