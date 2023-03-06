from itertools import combinations
from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n)]
viruses = []
answers = []
walls = 0

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] == 0: # 빈칸
            graph[i].append(0)
        elif temp[j] == 1:
            graph[i].append(1) # 벽
            walls += 1
        else:
            graph[i].append(2) # 바이러스
            viruses.append((i,j))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(virus):
    temp_graph = [[-1 for _ in range(n)] for _ in range(n)]
    for x,y in virus:
        temp_graph[x][y] = 0 # 출발 지점
    max_cnt = 0 # 최대 숫자
    
    queue = deque(virus)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 그래프 범위 충족
                # 원래 빈칸이면서 아직 방문한 적이 없을 때
                if graph[nx][ny] == 0 and temp_graph[nx][ny] == -1:
                    temp_graph[nx][ny] = temp_graph[x][y] + 1
                    queue.append((nx,ny))
                    max_cnt = max(max_cnt,temp_graph[nx][ny])
                # 비활성 바이러스이면서 아직 방문한 적이 없을 때 -> 업데이트 x
                elif graph[nx][ny] == 2 and temp_graph[nx][ny] == -1:
                    temp_graph[nx][ny] = temp_graph[x][y] + 1
                    queue.append((nx,ny))
    
    wall = 0 # 현재 그래프 내의 이동 불가능 지역
    for i in range(n):
        wall += temp_graph[i].count(-1) # 이동이 불가능한 칸

    if wall == walls: # 도달하지 못한 영역이 없는 경우
        answers.append(max_cnt) 

cases = combinations(viruses,m) # m개의 활성 바이러스
for case in cases:
    bfs(case)

if not answers:
    print(-1)
else:
    print(min(answers))