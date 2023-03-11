import sys

n = int(input())
k = int(input())

centers = sorted(list(map(int,sys.stdin.readline().strip().split()))) # 센터 위치 오름차순
dists = sorted([centers[i]-centers[i-1] for i in range(1,n)],reverse=True) # 거리 내림차순
print(sum(dists[k-1:]))