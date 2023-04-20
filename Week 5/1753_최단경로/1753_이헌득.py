import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
dist = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dist_now, now = heapq.heappop(q)
        if dist[now] < dist_now:
            continue
        for i in graph[now]:
            cost = dist_now+i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
        
for i in range(1,n+1):
    x = dist[i]
    if x == INF:
        print("INF")
    else:
        print(x)