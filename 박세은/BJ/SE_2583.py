from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 1
    count = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                q.append((nx, ny))
                count += 1
                arr[nx][ny] = 1
    count_list.append(count)


M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]
count_list = []

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            bfs(i, j)

print(len(count_list))
print(*sorted(count_list))
