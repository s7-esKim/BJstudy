'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
# 왼쪽 아래  오른쪽 위
import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())

arr = [[1]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(M-y2, M-y1):
            arr[y][x] = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(root):
    q = deque()
    q.append(root)
    cnt = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<= ni < M and 0 <= nj < N:
                if arr[ni][nj]:
                    arr[ni][nj] = 0
                    q.append((ni,nj))
                    cnt += 1
    return cnt

cnt_lst = []
for i in range(M):
    for j in range(N):
        if arr[i][j]:
            arr[i][j] = 0
            cnt = bfs((i,j))
            cnt_lst.append(cnt)

print(len(cnt_lst))
print(*sorted(cnt_lst))
