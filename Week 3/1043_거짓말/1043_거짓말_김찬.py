from collections import deque

n,m = map(int,input().split())
trues = list(map(int,input().split()))
knows = [False for _ in range(n+1)] # 진실을 아는 사람 체크
graph = [[] for _ in range(n+1)] # 사람 간 연결 그래프
parties = [] # 파티별 구성원 리스트

for idx in range(m):
    tmp_list = list(map(int,input().split()))
    num,people = tmp_list[0],tmp_list[1:]
    parties.append(people) # 파티 참여자 기록
    for i in range(len(people)):
        for j in range(i+1,len(people)): # 양방향 간선
            graph[people[i]].append(people[j])
            graph[people[j]].append(people[i])
graph = [list(set(x)) for x in graph] # 중복 제거

if trues == [0]: # 진실을 아는 사람이 없는 경우
    print(m)
    exit(0) # 프로그램 종료

for true in trues[1:]: # 진실을 아는 사람은 체크
    knows[true] = True

def bfs(x): # type(x) - list
    queue = deque(x) # 진실을 아는 사람 리스트
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not knows[next]:
                knows[next] = True # 진실을 아는 사람으로 추가
                queue.append(next) # 이 사람이 만날 사람 추가 탐색

# 처음부터 진실을 아는 사람들 리스트
bfs([x for x in range(1,len(knows)) if knows[x]])
# 0번을 제외한 숫자만 추출
knows = [x for x in range(1,len(knows)) if knows[x]]

cnt = 0 
for party in parties: # 각 파티별로
    if not (set(party) & set(knows)): # 아는 사람이 하나도 없다면
        cnt += 1 # 과장된 이야기 할 수 있는 파티 개수 증가
print(cnt)