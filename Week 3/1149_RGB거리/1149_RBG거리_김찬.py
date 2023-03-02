import sys # 빠른 입력

graph = []
n = int(input())
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip().split())))

dp = graph[0]
for idx in range(1,n):
    pre_red,pre_green,pre_blue = dp[0],dp[1],dp[2] # dp table에 저장된 값
    red,green,blue = graph[idx][0],graph[idx][1],graph[idx][2] # 현재 행

    dp[0] = red + min(pre_green,pre_blue) # 다른 색상 중 작은 값 더하기
    dp[1] = green + min(pre_red,pre_blue)
    dp[2] = blue + min(pre_red,pre_green)

print(min(dp))