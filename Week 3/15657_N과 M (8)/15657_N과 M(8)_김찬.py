n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

answers = []
def recipe(v):
    if len(v) == m: # m개를 다 뽑았으면 종료
        answers.append(v[:])
        return
    
    for idx in range(n):
        # 리스트 내 숫자보다 작은 경우는 패스
        if v and nums[idx] < v[-1]:
            continue
        else: # 리스트 내 숫자 이상인 경우 추가
            v.append(nums[idx])
        recipe(v) # 재귀
        v.pop() # 마지막 숫자 pop

recipe([]) # 공백 리스트로 시작

# 각 리스트의 모든 원소를 띄어쓰기로 구분하여 출력
for answer in answers: 
    print(*answer,sep=' ')