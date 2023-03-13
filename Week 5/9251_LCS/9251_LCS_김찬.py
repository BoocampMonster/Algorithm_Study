a = input()
b = input()

def lcs(a,b):
    m,n = len(a),len(b)

    dp = [[None for _ in range(n+1)] for _ in range(m+1)]

    for row in range(m+1):
        for col in range(n+1):
            if row == 0 or col == 0: # 둘 중 하나가 글자가 아닌 경우
                dp[row][col] = 0
            elif a[row-1] == b[col-1]: # 동일한 글자가 발견된 경우
                dp[row][col] = dp[row-1][col-1] + 1 # 직전 + 1
            else: # 동일한 글자가 아닌 경우 -> 현재까지의 최댓값 불러오기
                dp[row][col] = max(dp[row-1][col],dp[row][col-1])
    
    return dp[row][col]

print(lcs(a,b))