import sys

def main():
    n = int(sys.stdin.readline().strip())
    
    graph = []
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int,sys.stdin.readline().strip().split())))
    dp[0][0] = graph[0][0] # 맨 처음값

    if n == 1: # 한 개면 바로 종료
        print(dp[0][0])
        exit(0)
    elif n == 2: # 두 개도 바로 종료
        print(dp[0][0] + max(graph[1]))
        exit(0)
    
    # 두 번째 행까지 초기화
    dp[1][0],dp[1][1] = (dp[0][0]+graph[1][0]),(dp[0][0]+graph[1][1])
    for i in range(2,n): # 세 번째 행부터
        for j in range(i+1): # 3,4,5,..개를 확인
            if j == 0: # 첫 번째 열
                dp[i][j] = graph[i][j] + dp[i-1][j]
            elif j == i: # 중간인 경우
                dp[i][j] = graph[i][j] + dp[i-1][j-1]
            else: # 마지막 열
                dp[i][j] = max(graph[i][j]+dp[i-1][j-1],graph[i][j]+dp[i-1][j])
    
    print(max(dp[-1]))

if __name__ == "__main__":
    main()