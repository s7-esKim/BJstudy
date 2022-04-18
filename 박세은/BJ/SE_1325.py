from collections import deque
from sys import stdin
input = stdin.readline


def bfs(a):
    q = deque([a])
    count = 1
    visited = [0] * (N + 1)
    visited[a] = 1
    while q:
        x = q.popleft()
        for com in arr[x]:
            if visited[com] == 0:
                q.append(com)
                visited[com] = 1
                count += 1
    return count


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)


result = []
max_count = 0
for i in range(1, N+1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)
print(*result)
