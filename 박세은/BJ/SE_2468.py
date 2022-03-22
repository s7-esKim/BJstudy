N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_land = 0
for i in range(N):
    for j in range(N):
        if max_land < arr[i][j]:
            max_land = arr[i][j]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(a, b, water):
    stack = [(a, b)]
    visited[a][b] = 1

    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > water and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))


answer = 0
for i in range(max_land):
    visited = [[0]*N for _ in range(N)]
    count = 0

    for j in range(N):
        for k in range(N):
            if arr[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                count += 1
    if answer < count:
        answer = count
print(answer)