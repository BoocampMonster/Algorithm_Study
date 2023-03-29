c = int(input())
n = int(input())
matrix = [[0] * (c + 1) for _ in range(c + 1)]
q = []
for _ in range(n):
    x,y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
    if x == 1:
        q.append(y)
    elif y == 1:
        q.append(x)

infect = []
while len(q) != 0 :
    x = q.pop(0)
    for i in range(1,c+1):
        v = matrix[x][i]
        if v == 1:
            infect.append(i)
            q.append(i)
            matrix[x][i] = 0

print(len(set(infect))-1)