import sys

class WeightedUF():
    def __init__(self, length):
        self.parent = [-1 for _ in range(length)]
        
    def find(self, x):
        if self.parent[x] < 0: # root node
            return x
        else:
            y = self.find(self.parent[x])
            self.parent[x] = y
            return y
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y: return
        
        if self.parent[x] <= self.parent[y]: # 값이 작을수록 자식 노드가 많음
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y


if __name__=='__main__':
    input = lambda : sys.stdin.readline().strip()

    N, M = int(input()), int(input())
    connections = [list(map(int, input().split())) for _ in range(N)]
    plans = list(map(int, input().split()))
    uf = WeightedUF(N)
    # upper matrix
    for i in range(N):
        for j in range(i+1, N):
            if connections[i][j] == 1:
                uf.union(i, j)
                
    answers = set([uf.find(i-1) for i in plans])
    if len(answers) == 1:
        print('YES')
    else:
        print("NO")