import sys
from collections import deque
#섬의 조건
# 1. 자기 자신을 제외한 8방향이 바다로 둘러쌓이기
# 2. 몇개의 땅으로 이루어진 경우 8방향으로 건너갈 수 있으면 섬
# 3. 가로,세로, 대각선 이동 가능 <<< 8방향 델타
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

def BFS(x,y):
    global cnt
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0

    while queue:
        ci, cj = queue.popleft()

        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1:
                queue.append((ni, nj))
                arr[ni][nj] = 0

def DFS(x, y):
    arr[x][y] = 0
    for i in range(8):
        ni = x + di[i]
        nj = y + dj[i]
        if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1:
            DFS(ni, nj)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                # BFS(i,j)
                DFS(i,j)
    print(cnt)
