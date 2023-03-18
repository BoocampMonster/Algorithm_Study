import sys
import heapq

def main():
    V,E = map(int,sys.stdin.readline().strip().split()) # 정점, 간선
    K = int(sys.stdin.readline().strip()) # 시작점

    INF = int(1e9) # 초기값
    graph = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)

    for _ in range(E):
        u,v,w = map(int,sys.stdin.readline().strip().split())
        graph[u].append((v,w)) # (정점, 가중치)

    def dijkstra(start): # 최단경로 탐색
        queue = []
        heapq.heappush(queue,(0,start)) # (가중치, 정점)
        distance[start] = 0

        while queue:
            dist,now = heapq.heappop(queue)
            if distance[now] < dist: # 최단 경로가 아니라면
                continue

            for v,w in graph[now]:
                cost = dist + w # 현재 정점까지의 가중치 + 다음 정점까지의 가중치
                if cost < distance[v]: # 현재 정점까지의 가중치가 더 작다면
                    distance[v] = cost
                    heapq.heappush(queue,(cost,v))

    dijkstra(K)

    for num in range(1,V+1):
        if distance[num] == INF:
            print("INF")
        else:
            print(distance[num])


if __name__ == '__main__':
    main()