a = str(input())
b = str(input())

if len(a) < len(b):
    upper, under = b, a
else:
    upper, under = a, b
    
M, m = len(upper), len(under)   
if len(a) == 0 or len(b) == 0:
    print(M)
    exit(0)

for i in range(m):
    curr = under[i:]
    for idx in range(len(curr)):
        if upper[idx] == curr[idx]:
            if upper[idx] == "2":
                state = False
                break
        state=True
    if state:
        break
if not state :
    right = M+m
else:
    right = M+i

for i in range(M):
    curr = upper[i:]
    if len(curr) < m:
        l = len(curr)
    else:
        l = m
    for idx in range(l):
        if under[idx] == curr[idx]:
            if under[idx] == "2":
                state = False
                break
        state = True
    if state:
        break
if not state:
    left = M+m
else:
    if m+i < M:
        left = M
    else:
        left = m+i
        
print(min(left,right))