from typing import *

def solution(array:List[str]):
    s:List[str] = []
    score:int = 0
    for i, rod in enumerate(array):
        if rod == '(':
            s.append(rod)
        else:
            s.pop()
            if array[i-1] == '(': # 레이저 지이이이잉
                score += len(s)
            else: # 쇠막대기의 끝부분 도달
                score += 1
    
    return score

array = list(input())
print(solution(array))