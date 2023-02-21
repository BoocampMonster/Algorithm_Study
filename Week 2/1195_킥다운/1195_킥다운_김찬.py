a = input()
b = input()

answer = len(a) + len(b) # 최악의 경우
# 길이가 긴 것을 a, 짧은 것을 b로 설정
if len(a) < len(b):
    a,b = b,a
gap = len(a) - len(b)

# 길이가 짧은 것이 왼쪽에 길게 늘어지는 경우
# 000002112112112
# 221211200000000
for zero in range(len(b)-1,0,-1):
    # 0의 개수를 줄이며 길이가 동일한 문자열 쌍을 유지
    tmp_a = '0' * zero + a
    tmp_b = b + '0' * (zero+gap)
    
    flag = True # 이상 탐지 flag
    for up,down in zip(tmp_a,tmp_b):
        # 튀어나온 부분이 겹치면 불가능한 case
        if up == '2' and down == '2':
            flag = False
            break
    if flag: # 이상이 발견되지 않은 경우라면 정답 갱신
        answer = min(answer,len(tmp_a))
    if answer == len(a): # 최소 길이가 중간에 발견되면 종료
        print(answer)
        exit(0)

# 길이가 짧은 것이 오른쪽에 길게 늘어지는 경우    
# 211211211200000
# 000000002212112
for zero in range(len(b)-1,0,-1):
    # 0의 개수를 줄이며 길이가 동일한 문자열 쌍을 유지
    tmp_a = a + zero * '0'
    tmp_b = (zero+gap) * '0' + b

    flag = True # 이상 탐지 flag
    for up,down in zip(tmp_a,tmp_b):
        # 튀어나온 부분이 겹치면 불가능한 case
        if up == '2' and down == '2':
            flag = False
            break
    if flag: # 이상이 발견되지 않은 경우라면 정답 갱신
        answer = min(answer,len(tmp_a))
    if answer == len(a): # 최소 길이가 중간에 발견되면 종료
        print(answer)
        exit(0)
# 두 문자열이 완전히 겹쳐 있는 경우
# 2112112112
# 0022121120
for zero in range(gap,-1,-1):
    # 0의 개수를 줄이며 길이가 동일한 문자열 쌍을 유지  
    tmp_a = a
    tmp_b = '0'*(gap-zero) + b + '0'*zero

    flag = True # 이상 탐지 flag
    for up,down in zip(tmp_a,tmp_b):
        # 튀어나온 부분이 겹치면 불가능한 case
        if up == '2' and down == '2':
            flag = False
            break
    if flag:
        answer = min(answer,len(tmp_a))
    if answer == len(a): # 최소 길이가 중간에 발견되면 종료
        print(answer)
        exit(0)
# 최소 길이가 중간에 발견되지 않은 case
print(answer)