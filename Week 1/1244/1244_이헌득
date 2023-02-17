# Setting
n = int(input())
switch = list(map(int, input().split()))
m = int(input())
peoples = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    peoples.append(tmp)

# Solve
def man(state, number, n):
    idx = []
    tmp = 0
    while True:
        tmp += number
        if tmp > n :
            break
        idx.append(tmp-1)
    for i in idx:
        state[i] = abs(state[i]-1)
    return state

def woman(state, number, n):
    idx = [number-1]
    for i in range(1, n):
        b, a = number - i, number + i
        if b < 1 or a > n:
            break
        if state[b-1] != state[a-1]:
            break
        else:
            idx.append(b-1)
            idx.append(a-1)
    for i in idx:
        state[i] = abs(state[i]-1)
    return state

for people in peoples:
    sex, num = map(int,people)
    if sex == 1:
        switch = man(switch, num, n)
    else:
        switch = woman(switch, num, n)
    
count = 0  # 20개 출력을 위한 변수 선언
while count < len(switch):

    print(switch[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1