from collections import deque
import sys
sys.stdin = open('1.txt')


dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우 좌상/우상/좌하/우하
dy = [0, 0, -1, 1, -1, 1, -1 , 1] # 상하좌우 좌상/우상/좌하/우하


def bfs(xx, yy):
    arr[xx][yy] = 0
    q = deque()
    q.append([xx, yy])
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split()))for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

