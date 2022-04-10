import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    global answer
    q = deque([start])
    visited[start] = 1
    while q:
        x = q.popleft()
        group = visited[x]
        for i in arr[x]:
            if not visited[i]:
                q.append(i)
                if group == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == group:
                return False
    return True


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for j in range(1, V+1):
        if not visited[j]:
            answer = bfs(j)
            if not answer:
                break

    print('YES' if answer else 'NO')