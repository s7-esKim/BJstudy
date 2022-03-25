import sys
sys.stdin = open('1.txt')


dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우 좌상/우상/좌하/우하
dy = [0, 0, -1, 1, -1, 1, -1 , 1] # 상하좌우 좌상/우상/좌하/우하


def dfs(ii, jj):
    d_arr[ii][jj] = 0
    stack = [[ii, jj]]
    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and d_arr[nx][ny] == 1:
                d_arr[nx][ny] = 0
                stack.append([nx, ny])




while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    d_arr = [list(map(int, input().split()))for _ in range(h)]
    d_island = 0
    for i in range(h):
        for j in range(w):
            if d_arr[i][j] == 1:
                dfs(i, j)
                d_island += 1



    print(d_island)

