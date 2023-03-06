N, M = map(int, input().split())

def check(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

if N == 1:
    N += 1
for num in range(N, M+1):
    if check(num):
        print(num)