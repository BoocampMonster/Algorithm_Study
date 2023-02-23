n = int(input())
arr = list(map(int,input().split()))

dp = [1] * n # dp 테이블 초기화

for i in range(1, n): # 2번째 원소부터
    for j in range(0, i): # 그 이전 원소들과 비교하여
        if arr[i] > arr[j]: # 이전 원소보다 크다면
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))