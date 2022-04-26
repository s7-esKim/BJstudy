from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(i, j):
    visited[i][j] = 0
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

si = sj = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            si = i
            sj = j

bfs(si, sj)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 0

for i in visited:
    print(*i)