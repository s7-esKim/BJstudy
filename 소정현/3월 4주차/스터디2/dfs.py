'''
가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
'''
import sys
## dfs
input = sys.stdin.readline
# 1은 땅 2는 바다

di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, 1, -1, 1, -1, -1, 1]

def find_land():
    land_lst = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                land_lst.append((i,j))
    return land_lst

def dfs(i, j):
    cnt = 0
    for k in range(8):
        if 0 <= i+di[k] < h and 0 <= j+dj[k] < w and not visit[i+di[k]][j+dj[k]] and arr[i+di[k]][j+dj[k]]:
            visit[i+di[k]][j+dj[k]] = 1
            dfs(i+di[k], j+dj[k])
        else:
            cnt +=1
    if cnt == 8:
        return

def dfs(a, b):
    lst = [(a, b)]
    while lst:
        i, j = lst.pop()
        for k in range(8):
            if 0 <= i+di[k] < h and 0 <= j+dj[k] < w and not visit[i+di[k]][j+dj[k]] and arr[i+di[k]][j+dj[k]]:
                visit[i+di[k]][j+dj[k]] = 1
                lst.append((i+di[k], j+dj[k]))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    visit = [[0]*w for _ in range(h)]
    land_lst = find_land()
    cnt = 0
    for i, j in land_lst:
        if not visit[i][j]:
            visit[i][j] = 1
            dfs(i,j)
            cnt += 1
    print(cnt)

