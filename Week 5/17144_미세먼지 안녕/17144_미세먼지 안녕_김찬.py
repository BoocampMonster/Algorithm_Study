from copy import deepcopy
import sys

def main():
    R,C,T = map(int, input().split()) # 행,열,케이스
    machine = [] # 공기청정기
    graph = [] # 전체 격자판

    for i in range(R):
        temp = list(map(int, sys.stdin.readline().strip().split()))
        if temp[0] == -1: # 공기청정기
            machine.append(i)
        graph.append(temp)

    dx = [0,0,1,-1] # 우,좌,하,상
    dy = [1,-1,0,0]
    for i in range(T):
        dust_list = dust_where(graph,R,C)
        board = deepcopy(graph) # 임시 격자판 복사
        for x,y in dust_list:
            temp = graph[x][y]//5 # 확산량(원래 그래프)
            for j in range(4): # 4방향
                nx,ny = x+dx[j], y+dy[j]
                # 범위 만족 & 공기청정기 아닌 경우
                if 0<=nx<R and 0<=ny<C and graph[nx][ny] != -1:
                    board[nx][ny] += temp # 복사그래프
                    board[x][y] -= temp

        upper_x,lower_x= machine[0],machine[1] # 공기청정기

        for j in range(upper_x-1,0,-1): # 문제에서 주어진 것과 반대 순서로
            board[j][0] = board[j-1][0]
        for j in range(C-1):
            board[0][j] = board[0][j+1]
        for j in range(upper_x):
            board[j][-1] = board[j+1][-1]
        for j in range(C-1,1,-1):
            board[upper_x][j] = board[upper_x][j-1]
        board[upper_x][1] = 0 # 청정기 바로 옆

        for j in range(lower_x+1,R-1): # 문제에서 주어진 것과 반대 순서로
            board[j][0] = board[j+1][0]
        for j in range(C-1):
            board[-1][j] = board[-1][j+1]
        for j in range(R-1,lower_x,-1):
            board[j][-1] = board[j-1][-1]
        for j in range(C-1,1,-1):
            board[lower_x][j] = board[lower_x][j-1]
        board[lower_x][1] = 0 # 청정기 바로 옆
        
        graph = board # 원래 그래프로 가져오기
    print(sum(sum(graph,[]))+2) # 최종 결과 + 2(공기청정기)

def dust_where(graph,R,C):
    dust_list = []
    for row in range(R): # 그래프 탐색
        for col in range(C):
            if graph[row][col] != 0 and graph[row][col] != -1:
                dust_list.append((row,col)) # 미세먼지 위치
    return dust_list

if __name__ == "__main__":
    main()