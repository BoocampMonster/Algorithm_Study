import sys
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    position = [0] * (n+1)
    for i in range(n):
        position[in_order[i]] = i # inorder에서의 인덱스를 저장

    answer = []
    def preorder(in_start,in_end,post_start,post_end):
        if (in_start > in_end) or (post_start > post_end):
            return

        root = post_order[post_end]
        size = position[root] - in_start
        answer.append(root)
        
        preorder(in_start, position[root]-1, post_start, post_start+size-1) # 왼쪽
        preorder(position[root]+1, in_end, post_start+size, post_end-1) # 오른쪽

    preorder(0,n-1,0,n-1)
    print(*answer)

if __name__ == '__main__':
    main()