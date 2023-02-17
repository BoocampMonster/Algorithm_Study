from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()
T = int(input())

for i in range(T):
    cnt = 0
    N, target = map(int, input().split())
    q = deque(list(map(int, input().split())))
    while q:
        max_value = max(q)
        p = q.popleft()
        if p < max_value: # 다시 큐에 넣기
            q.append(p)
            target = (target-1) % len(q)
        elif target != 0: # 프린트하지만 타겟은 아닌 경우
            cnt += 1
            target = (target-1) % len(q)
        else: # 프린트가 타겟인 경우
            cnt += 1
            break
    print(cnt)