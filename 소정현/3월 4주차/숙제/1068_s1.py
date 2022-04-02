'''
4
-1 0 1 2
2
# 일직선
1
-1
0
# 정답 0
2
-1 0
1
# 정답 1
5
-1 0 0 1 1
0
0인데 1나옴
'''

import sys
input = sys.stdin.readline

N = int(input())
connect_node = list(map(int, input().split())) # input값
delete_node_num = int(input())
connect_lst = [[] for _ in range(N)] # node들마다 연결되있는 하위 노드들을 추가할 리스트

start = 0

for i in range(N):
    if connect_node[i] != -1:
        connect_lst[connect_node[i]].append(i)
    else:
        start = i # -1인 지점은 start로 잡기

cnt = 0
check = True
if not connect_lst[start]:
    # cnt += 1
    if N == 1:
        cnt = -1
    check = False

delete_node = []

def del_node(T): # 삭제할 노드를 list에 추가하기
    delete_node.append(T)
    if connect_lst[T]:
        for i in connect_lst[T]:
            del_node(i)


def node_delete(node):
    for i in range(len(connect_lst)):
        if node in connect_lst[i]:
            connect_lst[i].remove(node) # 추가로 node지우기

def count_node(T):
    global cnt

    if connect_lst[T]: # 만약에 T가 node가 있으면 cnt안셈
        for i in connect_lst[T]:
            count_node(i)
    else: # 만약에 T에 연결된 하위노드가없으면 cnt + 1
        cnt += 1

del_node(delete_node_num)

for i in delete_node: # 그 노드들을 빈리스트로 만들기
    connect_lst[i] = []

node_delete(delete_node_num)


if not connect_lst[start] and check:
    cnt = 1
else:
    count_node(start)

if start == delete_node_num:
    cnt = 0
print(cnt)