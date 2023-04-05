n, m = map(int, input().split())
knows = list(map(int, input().split()))
if len(knows) == 1:
    print(m)
    exit(0)
groups = []
knows = knows[1:]
cnt = 0
matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    tmp = (list(map(int, input().split())))
    groups.append(tmp[1:])
    for x in tmp[1:]:
        for y in tmp[1:]:
            matrix[x][y] = 1
            matrix[y][x] = 1
linked = []
for know in knows:
    q = [know]
    while q:
        tmp = q.pop(0)
        for i in range(1,n+1):
            x = matrix[tmp][i]
            if x == 1:
                q.append(i)
                linked.append(i)
                matrix[tmp][i] = 0

for group in groups:
    tmp = set(linked) & set(group)
    if len(tmp) > 0:
        cnt += 1        

print(m-cnt)