from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tomato = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append([i, j])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while tomato:
    x, y = tomato.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                tomato.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1

answer = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    answer = max(answer, max(i))
print(answer-1)