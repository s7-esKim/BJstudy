import sys
from collections import deque
input = sys.stdin.readline

V = int(input())



connect_lst = [[] for _ in range(V+1)]

for i in range(V):
    tree_lst = list(map(int, input().split()))
    j = 1
    while tree_lst[j] != -1:
        connect_lst[i+1].append((tree_lst[j],tree_lst[j+1]))
        j += 2

def max_dist_v():
    max_dist = 0
    for i in range(len(connect_lst))

visit = [0]*(V+1)

def dfs(T, dist, visit):
    global max_length
    if dist > max_length:
        max_length = dist
    for i, j in connect_lst[T]:
        if not visit[i]:
            visit[i] = 1
            dfs(i, dist+j, visit)

visit[t] = 1
max_length = 0
dfs(t, 0, visit)
print(max_length)