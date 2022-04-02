#bfs
import sys
from collections import deque
input = sys.stdin.readline

di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, 1, -1, 1, -1, -1, 1]

def find_land():
    land_lst = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                land_lst.append((i,j))
    return land_lst

def bfs(a, b):

    queue = deque()
    queue.append((a,b))
    while queue:
        i, j = queue.popleft()
        for k in range(8):
            if 0 <= i + di[k] < h and 0 <= j + dj[k] < w and (i+di[k], j+dj[k]) not in visit_lst and arr[i + di[k]][j + dj[k]]:
                queue.append((i+di[k], j+dj[k]))
                visit_lst.append((i+di[k], j+dj[k]))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    land_lst = find_land()

    tot_lst = []
    visit_lst = []
    cnt = 0
    for i, j in land_lst:
        if (i,j) not in visit_lst:
            visit_lst.append((i,j))
            bfs(i, j)
            cnt += 1
    print(cnt)