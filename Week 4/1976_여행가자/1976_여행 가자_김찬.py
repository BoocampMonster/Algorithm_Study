n = int(input())
m = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

plan = list(map(int,input().split()))
parent = [x for x in range(n+1)] # 0부터 n까지

def find_parent(x):
    if parent[x] != x: # 재귀적으로 부모 노드 탐색
        parent[x] = find_parent(parent[x])
    return parent[x] # 최상단 부모 노드 반환

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 작은 숫자가 큰 숫자의 부모
        parent[b] = a
    else:
        parent[a] = b

for i in range(n-1): # 그래프 우상단 삼각형만 탐색
    for j in range(i+1,n):
        if graph[i][j] == 1:
            union_parent(i+1,j+1)

for i in range(len(plan)-1): # 부모가 동일하면 continue
    if find_parent(plan[i]) == find_parent(plan[i+1]):
        continue
    else: # 부모가 다른 경우 존재하면 프로그램 종료
        print('NO')
        exit()
print('YES')