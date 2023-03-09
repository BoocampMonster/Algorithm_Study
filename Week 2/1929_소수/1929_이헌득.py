n,m = map(int, input().split())
if n ==1 :
    n = 2
    
v = []
r = 2
while True:
    if r**2 > m:
        break
    r += 1

for i in range(2,r+1):
    if i not in v:
        tmp = i * 2
        while tmp <= m:
            v.append(tmp)
            tmp += i
            
answer = list(set(range(n,m+1)) - set(v))
for x in answer:
    print(x)