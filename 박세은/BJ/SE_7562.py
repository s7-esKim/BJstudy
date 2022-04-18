from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(a, b):
    global c, d
    q = deque([(a, b)])
    arr[a][b] = 1
    while q:
        x, y = q.popleft()
        if x == c and y == d:
            return arr[x][y] - 1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(bfs(a, b))
