from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(x,y,t,visited):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci +di[k]
            nj = cj +dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] > t and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))



max_value = 0
for i in range(N):
    for j in range(N):
        if max_value < arr[i][j]:
            max_value = arr[i][j]

safe_region = 0
for t in range(max_value):
    visited = [[0] * N for _ in range(N)]
    temp = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] > t and visited[x][y] == 0:
                bfs(x,y,t,visited)
                temp += 1
    if safe_region < temp:
        safe_region = temp

print(safe_region)