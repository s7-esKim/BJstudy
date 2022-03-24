import sys
sys.setrecursionlimit(10**6)

dr = [1, 1, 0, -1, -1, -1, 0, 1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(r,c):
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
            arr[nr][nc] = -1
            dfs(nr, nc)

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    arr = [list(map(int,input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)