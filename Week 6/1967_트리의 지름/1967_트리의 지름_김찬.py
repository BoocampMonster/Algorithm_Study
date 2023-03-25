import sys
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    visited = [False] * (n+1) # 방문 여부
    distance = [0] * (n+1) # 이동 거리
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        parent, child, weight = map(int, sys.stdin.readline().strip().split())
        graph[parent].append((weight, child))
        graph[child].append((weight, parent))

    dfs(1, graph, visited, distance) # 랜덤 시작

    v = max(range(1,n+1), key=lambda x: distance[x]) # 가장 먼 노드 구하기

    visited = [False] * (n+1) # 방문 여부 초기화
    distance = [0] * (n+1) # 거리 초기화

    dfs(v, graph, visited, distance) # 가정 먼 노드로부터 가장 먼 노드 구하기

    u = max(range(1,n+1), key=lambda x: distance[x])

    print(distance[u])

def dfs(x, graph, visited, distance):
    visited[x] = True

    for weight, nx in graph[x]:
        if not visited[nx]:
            distance[nx] = distance[x] + weight
            dfs(nx, graph, visited, distance)

if __name__ == '__main__':
    main()