import sys
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    tree = {}

    for _ in range(n):
        root, left, right = input().split() # 루트, 좌, 우
        tree[root] = (left,right)
    
    pre_answer, in_answer, post_answer = [], [], []

    pre_order(tree, 'A', pre_answer)
    in_order(tree, 'A', in_answer)
    post_order(tree, 'A', post_answer)

    print(''.join(pre_answer))
    print(''.join(in_answer))
    print(''.join(post_answer))

def pre_order(tree, root, pre_answer):
    if root != '.':
        pre_answer.append(root) # 루트
        pre_order(tree, tree[root][0], pre_answer) # 좌
        pre_order(tree, tree[root][1], pre_answer) # 우

def in_order(tree, root, in_answer):
    if root != '.':
        in_order(tree, tree[root][0], in_answer) # 좌
        in_answer.append(root) # 루트
        in_order(tree, tree[root][1], in_answer) # 우

def post_order(tree, root, post_answer):
    if root != '.':
        post_order(tree, tree[root][0], post_answer) # 좌
        post_order(tree, tree[root][1], post_answer) # 우
        post_answer += root # 루트

if __name__ == '__main__':
    main()