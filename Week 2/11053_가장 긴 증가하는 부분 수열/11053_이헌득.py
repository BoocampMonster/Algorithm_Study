n = int(input())
num_list = list(map(int, input().split()))

table = [1] * n

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            table[i] = max(table[i], table[j]+1)
print(max(table))