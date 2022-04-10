from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    while q:
        x, y, wall = q.popleft()
        if x == N-1 and y == M-1:
            return visit[x][y][wall] + 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and wall == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif arr[nx][ny] == 0 and visit[nx][ny][wall] == 0:
                    visit[nx][ny][wall] = visit[x][y][wall] + 1
                    q.append([nx, ny, wall])
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs())