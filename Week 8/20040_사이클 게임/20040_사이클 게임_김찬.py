import sys
sys.setrecursionlimit(10**6)

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    parents = [x for x in range(n)] # 부모 노드 리스트

    def root(x):
        if x != parents[x]: # 자기 자신이 될 때까지 재귀
            parents[x] = root(parents[x])
        return parents[x]

    def union(a,b,cnt):
        global answer
        a, b = root(a), root(b)
        if a != b: # 작은 것이 부모, 큰 것이 자식
            parents[max(a,b)] = min(a,b)
        elif answer == 0: # 최초의 사이클
            answer = cnt

    for cnt in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        union(a,b,cnt+1)
    
    print(answer)

if __name__ == '__main__':
    answer = 0
    main()