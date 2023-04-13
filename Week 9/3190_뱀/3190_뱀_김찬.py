from collections import deque

def main():
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]

    k = int(input())
    for _ in range(k):
        r, c = map(int, input().split())
        board[r-1][c-1] = -1 # 사과 위치 기록

    turns = {} # 방향 전환 딕셔너리
    l = int(input())
    for _ in range(l):
        x, c = input().split()
        turns[int(x)] = c
    
    def turn(alpha,dir):
        if alpha == 'L':  # 왼쪽이면 -1
            dir = (dir-1) % 4
        else: # 오른쪽이면 +1
            dir = (dir+1) % 4
        return dir

    cnt = 0
    queue = deque([(0,0)])
    board[0][0] = 1 # 시작점
    x,y = 0,0

    dx = [0,1,0,-1] # 방향 전환
    dy = [1,0,-1,0]
    dir = 0

    while True:
        cnt += 1
        x += dx[dir] # 이동
        y += dy[dir]
        
        if x < 0 or x >= n or y < 0 or y >= n:
            break # 범위 벗어나는 경우

        if board[x][y] == -1: # 사과인 경우
            board[x][y] = 1
            queue.append((x,y))
            if cnt in turns: # 방향 전환 확인
                dir = turn(turns[cnt],dir)
        
        elif board[x][y] == 0: # 빈칸인 경우
            board[x][y] = 1
            queue.append((x,y))
            ox,oy = queue.popleft()
            board[ox][oy] = 0 # 비워주기
            if cnt in turns: # 방향 전환 확인
                dir = turn(turns[cnt],dir)
        
        else:
            break

    print(cnt)

if __name__ == '__main__':
    main()