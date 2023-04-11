n = int(input())
arr = list(map(int, input().split()))
limit = int(input())

M = max(arr)

if sum(arr) - limit <= 0 :
    print(M)

else:
    start = 0
    end = M
    answer = 0
    while start <= end:
        tmp = 0
        pivot = (start+end) // 2
        
        # calculate
        for x in arr :
            if x <= pivot:
                tmp += x
            else:
                tmp += pivot
            
        # print(pivot, tmp)
        if tmp <= limit :
            start = pivot + 1
            answer = pivot
        else:
            end = pivot - 1
            
    print(answer)