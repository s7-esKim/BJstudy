import sys
sys.stdin = open('1.txt')
from pprint import pprint
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    # 좌표값 넣어주고 1로 바꿔놓기 영역 넓이 구해야 하니까 cnt + 1
    q.append([x, y])
    arr[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1

    return cnt

m, n, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 직사각형그리기
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1



result = []
#정답을 담을 변수
for i in range(n):
    for j in range(m):
        # 빈영역이면 bfs
        if arr[i][j] == 0:
            result.append(bfs(i, j))


print(len(result))
print(*sorted(result))


