import sys

def main():
    n, m = map(int, input().split())

    graph = [[0] * (n+1)]
    for _ in range(n):
        nums = [0] + list(map(int, sys.stdin.readline().strip().split()))
        graph.append(nums)
    
    for row in range(1,n+1):
        for col in range(2,n+1):
            graph[row][col] += graph[row][col-1] # 열 누적
    
    for row in range(2,n+1): # 행 누적
        for col in range(1,n+1):
            graph[row][col] += graph[row-1][col]

    for _ in range(m): # 누적합 계산(중복은 덧셈)
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        print(graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1])

if __name__ == '__main__':
    main()