m,n = map(int,input().split())

sosu = [1 for _ in range(n+1)]
sosu[1] = 0

for num in range(2,int(n**0.5)+1):
    if sosu[num]: # 배수로 제거되지 않은 숫자인 경우
        # 이 숫자의 배수는 전부 0으로 바꿔준다
        for multiple in range(num+num,n+1,num):
            sosu[multiple] = 0

# 배수가 아니라서 1로 남아있던 숫자를 모두 출력
for idx in range(m,n+1):
    if sosu[idx]: print(idx)