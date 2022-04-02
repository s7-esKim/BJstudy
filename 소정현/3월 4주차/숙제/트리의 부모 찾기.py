import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input()) # 노드의 개수

root = 1

node_lst = [0]*(N+1)
node_lst[1] = 1

connect_lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    connect_lst[j].append(i)
    connect_lst[i].append(j)


def parent_node(i):
    if connect_lst[i]:
        for j in connect_lst[i]:
            if not node_lst[j]:
                node_lst[j] = i
                parent_node(j)

parent_node(1)
node_lst = node_lst[2:]
for i in node_lst:
    print(i)