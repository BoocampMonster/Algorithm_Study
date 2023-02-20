from typing import *

def upper_below(a:str, b:str) -> Tuple[str]:
    '''길이가 긴 스트링을 below로 설정하는 함수'''
    if len(a) < len(b):
        return a, b
    else:
        return b, a
    
def kick_down(upper:str, below:str):
    '''upper와 below가 맞물리는 모든 경우의 수 탐색'''
    length = 200
    len_u, len_b = len(upper), len(below)
    board = '0' * len_u + below + '0' * len_u # upper이 들어갈 수 있는 모든 경우의 수
    for b_i in range(len_b+len_u):
        is_kick_down = True
        for u_i, u in enumerate(upper):
            if board[b_i+u_i] == '2' and u == '2': # 이가 서로 맞물리는 경우
                is_kick_down = False
                break
        if is_kick_down:
            if b_i <= len_u: # upper가 좌측
                sub_below = board[b_i:len_b+len_u]
            elif len_u < b_i < len_b: # upper가 below안에 포함
                sub_below = below
            else: # upper가 우측
                sub_below = board[len_u:b_i+len_u]
                
            length = min(len(sub_below) ,length)
                
    return length
    
if __name__=='__main__':
    print(kick_down(*upper_below(input(), input())))