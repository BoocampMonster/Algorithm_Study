import sys

n,k = map(int,sys.stdin.readline().rstrip().split())
bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

items = [(0,0)]
for i in range(n):
    w,v = map(int,sys.stdin.readline().rstrip().split())
    items.append((w,v)) # weight,value

for row in range(1,n+1):
    for col in range(1,k+1):
        weight = items[row][0] # 넣으려는 아이템의 무게
        value = items[row][1] # 넣으려는 아이템의 가치

        if col < weight: # col:현재 가방에 담을 수 있는 최대 무게
            bag[row][col] = bag[row-1][col] # 직전의 가방 무게를 그대로 가져온다
        else: # 현재 아이템을 넣는 경우 or 현재 아이템을 담지 않는 경우 중 큰 값을 가져온다
            bag[row][col] = max(bag[row-1][col],bag[row-1][col-weight]+value)

print(bag[n][k])