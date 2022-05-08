import sys
input = sys.stdin.readline
from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dzx = [-2, -1, 1, 2, 2, 1, -1, -2]
dzy = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs():
    q = deque([(0, 0, K)])
    while q:
        # k는 말처럼 뛸 수 있는 횟수
        x, y, k = q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if arr[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    q.append((nx, ny, k))
        if k > 0:
            for i in range(8):
                nx = x + dzx[i]
                ny = y + dzy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == 0 and visited[nx][ny][k-1] == 0:
                        visited[nx][ny][k-1] = visited[x][y][k] + 1
                        q.append((nx, ny, k-1))
    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
print(bfs())
