from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(x, y):
    arr[x][y] = 2
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append([nx, ny])


while True:
    w, h = map(int, input().split())
    if w == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                answer += 1
                bfs(i, j)
    print(answer)