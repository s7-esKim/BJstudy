# T = int(input())
# for t in range(T):
#     M, N, K = map(int, input().split())
#     chuchu = [[0] * M for _ in range(N)]
#     visit = [[0] * M for _ in range(N)]
#
#     for k in range(K):
#         j, i = map(int,input().split())
import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= ny < N) and (0 <= nx < M):
      if cabbage_field[ny][nx] == 1:
        cabbage_field[ny][nx] = -1
        dfs(ny, nx)

T = int(input())
counts = []

for _ in range(T):
  M, N, K = map(int, input().split())
  cabbage_field = [[0] * (M) for _ in range(N)]
  count = 0

  for _ in range(K):
    x, y = map(int, input().split())
    cabbage_field[y][x] = 1

  for y in range(N):
    for x in range(M):
      if cabbage_field[y][x] == 1:
        dfs(y, x)
        count += 1
  counts.append(count)

for cnt in counts:
  print(cnt)