import sys

class WeightedUF():
    def __init__(self, length:int) -> None:
        self.parent = [-1] * length
    
    def find(self, x:int) -> int:
        if self.parent[x] < 0: # root node
            return x
        else:
            y = self.find(self.parent[x])
            self.parent[x] = y
            return y
    
    def union(self, x:int, y:int) -> None:
        x = self.find(x)
        y = self.find(y)
        
        if x == y: return
        
        if self.parent[x] <= self.parent[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y

if __name__=='__main__':
    input = lambda: sys.stdin.readline().strip()
    computers = int(input())
    connected = int(input())
    
    uf = WeightedUF(computers+1)
    for _ in range(connected):
        p, q = map(int, input().split())
        uf.union(p, q)
        
    print((uf.parent[uf.find(1)] + 1) * -1)
