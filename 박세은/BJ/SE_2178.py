N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
stack = [(0, 0)]
count = 0

while stack:
    x, y = stack.pop(0)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1:
                stack.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
print(arr[N-1][M-1])