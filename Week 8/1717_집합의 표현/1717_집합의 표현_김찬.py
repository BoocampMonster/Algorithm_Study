import sys
sys.setrecursionlimit(10**6)

def main():
    n, m = map(int, input().split())
    parents = [x for x in range(n+1)] # 부모 노드 저장

    def find(x): # 부모 찾기
        if parents[x] != x: # 자기자신과 같아질 때까지
            parents[x] = find(parents[x])
        return parents[x]

    def union(a, b): # a,b 합치기
        a, b = find(a), find(b)
        if a < b: # 작은 숫자가 부모
            parents[b] = a
        else:
            parents[a] = b

    def connected(a, b): # 부모 같은지 확인
        return find(a) == find(b)

    for _ in range(m):
        x, a, b = map(int, sys.stdin.readline().strip().split())
        if x == 0:
            union(a, b)
        else:
            print("YES" if connected(a, b) else "NO")

if __name__ == '__main__':
    main()