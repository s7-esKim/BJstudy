from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, area):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] >= area and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_num = min(min(arr))
max_num = max(max(arr))

max_area = min_num
for i in range(min_num, max_num+1):
    visited = [[0]*N for _ in range(N)]
    temp = 0
    for j in range(N):
        for k in range(N):
            if arr[j][k] >= i and visited[j][k] == 0:
                bfs(j, k, i)
                temp += 1
    if temp > max_area:
        max_area = temp
print(max_area)
