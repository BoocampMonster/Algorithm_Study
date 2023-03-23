import sys
from heapq import heappush, heappop

def main():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    distance = [10**9] * (n+1) # 최댓값으로 초기화

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b,c)) # 출발, 도착, 비용

    start, end = map(int,input().split()) # 출발, 도착

    def dijkstra(start):
        queue = []
        distance[start] = 0 # 시작점 비용
        heappush(queue,(0,start))

        while queue:
            cost, x = heappop(queue) # 현재까지의 비용, 현재 노드
            if cost > distance[x]: # 현재까지의 비용이 더 크면 갱신 불필요
                continue

            for nx, ncost in graph[x]: # 이동 가능 노드, 추가 비용
                if cost + ncost < distance[nx]: # 현재까지 비용 + 추가 비용
                    distance[nx] = cost + ncost
                    heappush(queue, (distance[nx],nx)) # 비용기준 push
    
    dijkstra(start)
    print(distance[end])

if __name__ == '__main__':
    main()