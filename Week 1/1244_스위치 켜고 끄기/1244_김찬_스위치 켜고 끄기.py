k = int(input())
switches = list(map(int,input().split()))
n = int(input())
for i in range(n):
    sex,num = map(int,input().split()) # 성별,숫자 입력
    if sex == 1: # 남자인 경우
        for j in range(num-1,k//num*num,num): # 배수 인덱스
            if switches[j] == 0: # 스위치 변환
                switches[j] = 1
            else: switches[j] = 0
    else: # 여자인 경우
        num -= 1 # 인덱스 변환
        tmp = 0 # 좌우로 넓힐 칸 숫자
        # 인덱스 범위를 만족하는 동안 반복
        while (num-tmp) >= 0 and (num+tmp) < k:
            # 기준 인덱스 좌우가 동일하다면 범위 증가
            if switches[num-tmp] == switches[num+tmp]:
                tmp += 1
            else: # 동일하지 않으면 이전 범위로 축소
                tmp -= 1
                break
        # 인덱스를 벗어나서 중단된 경우 범위 조정
        if (num-tmp) < 0 or (num+tmp) >= k:
            tmp -= 1
        # 기준 인덱스 중심으로 스위치 변환
        for j in range(num-tmp,num+tmp+1):
            if switches[j] == 0:
                switches[j] = 1
            else: switches[j] = 0

cnt = 0
for i in range(len(switches)-1):
    print(switches[i],end=' ') # 띄어쓰기 옵션
    cnt += 1
    # 20개마다 줄 바꾸고 카운트 초기화
    if cnt == 20: 
        cnt = 0
        print('')
print(switches[-1]) # 마지막 한 개는 띄어쓰기 없이 따로 출력