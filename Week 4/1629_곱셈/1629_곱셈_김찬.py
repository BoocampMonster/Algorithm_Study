a,b,c = map(int,input().split())

def div(a,b,c):
    if b == 1:
        return a % c

    tmp = div(a,b//2,c)

    if b % 2 == 1:
        return tmp**2 * a % c
    else:
        return tmp**2 % c

print(div(a,b,c))