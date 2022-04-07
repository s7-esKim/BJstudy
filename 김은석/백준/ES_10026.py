from copy import deepcopy
from collections import deque

def bfs(i, j, lst, color):
    queue = deque()
    queue.append((i,j))

    while queue:
        ci, cj = queue.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] == color:
                    lst[ni][nj] = 0
                    queue.append((ni,nj))


N = int(input())
p1 = [list(map(str, input())) for _ in range(N)]
p2 = deepcopy(p1)

for i in range(N):
    for j in range(N):
        if p2[i][j] == 'G':
            p2[i][j] = 'R'

cnt1 = 0                            # 일반
cnt2 = 0                            # 적록색약
for i in range(N):
    for j in range(N):
        if p1[i][j] != 0:
            cnt1 += 1
            bfs(i, j, p1, p1[i][j])

        if p2[i][j] != 0:
            cnt2 += 1
            bfs(i, j, p2, p2[i][j])

print(cnt1, cnt2)

