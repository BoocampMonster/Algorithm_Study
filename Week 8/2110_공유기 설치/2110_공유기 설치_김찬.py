import sys

def main():
    N,C = map(int, input().split())

    house = []
    for _ in range(N):
        house.append(int(sys.stdin.readline().strip()))
    house.sort()
    
    answer = 0
    left, right = 1, house[-1]-1
    while left <= right: # 간격의 최소/최대가 곧 탐색 범위
        gap = (left+right) // 2 # 간격
        cur = house[0] # 공유기 설치 위치
        cnt = 1 # 공유기 설치 대수

        for i in range(1,N):
            if house[i] <= cur + gap:
                cur = house[i] # 공유기 위치 갱신
                cnt += 1 # 공유기 설치 대수 증가
        
        if cnt <= C: # 공유기 충분 -> 간격 늘리기
            left = gap + 1
            answer = gap
        else: # 공유기 부족 -> 간격 줄이기
            right = gap - 1
    
    print(answer)

if __name__ == '__main__':
    main()