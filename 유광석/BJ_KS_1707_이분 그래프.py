import sys
from collections import deque

# def find(x):
#     while rep[x] != x:
#         x = rep[x]
#     return x

def BFS(s):
    global flag

    q = deque()
    q.append(s)

    while q:
        v = q.popleft()

        for nv in lst[v]:
            if not visited[nv]:
                visited[nv] = -1 * visited[v]
                q.append(nv)
                continue

            if visited[nv] == visited[v]:
                flag = False

        
for _ in range(int(input())):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    lst = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    visited[0] = 2
    for i in range(E):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        lst[v1].append(v2)
        lst[v2].append(v1)

    flag = True
    for i in range(V+1):
        if not visited[i]:
            visited[i] = 1
            BFS(i)

    if flag:
        print('YES')
    else:
        print('NO')