def idxing(idx, num_list):
    if idx == 0:
        return len(num_list) -1
    return idx - 1
    
T = int(input())
# n, idx = map(int, input().split())

for _ in range(T):
    n, idx = map(int,input().split(' '))
    num_list = list(map(int,input().split(' ')))
    M = max(num_list)
    place = 1
    while True:
        tmp = num_list.pop(0)
        if M != tmp:
            num_list.append(tmp)
            idx = idxing(idx, num_list)
        else:
            if idx == 0:
                break
            else:
                M = max(num_list)
                place += 1
                idx -= 1
    print(place)