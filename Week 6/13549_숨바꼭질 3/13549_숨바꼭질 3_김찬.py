import heapq

def main():
    n,k = map(int,input().split())
    limit = 10**5 + 1 # 최댓값
    INF = 10**9 # 비용 초기화
    arr = [INF] * (limit+1) 
    arr[n] = 0

    hq = []
    heapq.heappush(hq, (0,n))

    while hq: # 다익스트라
        cost, x = heapq.heappop(hq)
        if x == k: # 목표에 도달하면
            print(cost)
            exit(0)

        # (우로 이동, 좌로 이동, 순간 이동)
        for nx,ncost in ((x+1,1), (x-1,1), (x*2,0)):
            # 범위 만족 & 기존보다 효율적
            if 0 <= nx < limit and cost + ncost < arr[nx]:
                arr[nx] = cost + ncost # 갱신
                heapq.heappush(hq, (arr[nx], nx))
    
    print(arr[k])
    
if __name__ == "__main__":
    main()