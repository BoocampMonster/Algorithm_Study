def main():
    n,m = map(int,input().split())
    # 오름차순 정렬(중복 제거)
    nums = sorted(list(set(list(map(int,input().split())))))
    answers= []

    def dfs(arr):
        if len(arr) == m: # 길이가 m이면 종료
            answers.append(arr[:])
            return
        
        for idx in range(len(nums)):
            # 배열이 비어있거나 마지막 숫자 이상인 경우에만
            if not arr or arr[-1] <= nums[idx]:
                arr.append(nums[idx])
                dfs(arr)
                arr.pop()

    dfs([])

    for answer in answers:
        print(*answer)

if __name__ == '__main__':
    main()