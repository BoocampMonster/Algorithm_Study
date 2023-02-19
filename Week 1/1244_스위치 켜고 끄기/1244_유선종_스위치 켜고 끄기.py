import sys
from typing import *

def recursive(idx:int, depth:int=1) -> List[int]:
    if idx-depth>=0 and idx+depth<len(switches):
        if switches[idx-depth] != switches[idx+depth]:
            switches[idx] = switches[idx]^1
        else:
            switches[idx-depth], switches[idx+depth] = switches[idx-depth]^1, switches[idx+depth]^1
            recursive(idx, depth+1)
    else:
        switches[idx] = switches[idx]^1
        
if __name__=='__main__':
    sys.setrecursionlimit(10*8)
    input = lambda: sys.stdin.readline().strip()

    S = int(input())
    switches = list(map(int, input().split()))
    N = int(input())
    command = [tuple(map(int, input().split())) for _ in range(N)]

    for sex, idx in command:
        if sex == 1: # 남자일 경우
            for idx in range(idx-1, S, idx):
                switches[idx] = switches[idx]^1
        elif sex == 2: # 여자일 경우
            recursive(idx-1, 1)

    tmp = []
    for i in range(len(switches)):
        tmp.append(str(switches[i]))
        if len(tmp) == 20:
            print(*tmp)
            tmp = []
    if tmp:
        print(*tmp)