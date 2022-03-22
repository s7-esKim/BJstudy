from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(root, safe_area):
    queue = deque()
    queue.append(root)

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:
                if arr[i+di[k]][j+dj[k]] >= safe_area and not visit[i+di[k]][j+dj[k]]:
                    queue.append((i+di[k], j+dj[k]))
                    visit[i+di[k]][j+dj[k]] = 1

min_arr = min(map(min, arr))
max_arr = max(map(max, arr))
max_safe_zone = 0

for safe_area in range(min_arr, max_arr+1):
    visit = [[0] * N for _ in range(N)]
    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= safe_area and not visit[i][j]:
                bfs((i,j), safe_area)
                safe_zone += 1
    if max_safe_zone <= safe_zone:
        max_safe_zone = safe_zone
    # else:
    #     break
print(max_safe_zone)