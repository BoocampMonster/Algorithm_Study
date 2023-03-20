import sys
import heapq

def main():
    n = int(input())
    m = int(input())
    
    INF = int(1e9) # 초깃값
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b: # 자기 자신으로 갈 때는 0
                graph[a][b] = 0

    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().strip().split())
        if c < graph[a][b]: # 기존 비용보다 작을 때만 업데이트
            graph[a][b] = c

    for k in range(1,n+1): # 중간 노드
        for a in range(1,n+1): # 출발 노드
            for b in range(1,n+1): # 도착 노드
                # 출발 - 도착 vs 출발 - 중간 - 도착
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] == INF: # 이동 불가능한 경우
                print(0,end=' ')
            else:
                print(graph[a][b],end=' ')
        print() # 줄바꿈

if __name__ == '__main__':
    main()