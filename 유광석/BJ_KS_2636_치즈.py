from collections import deque
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

def now_cheese(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
    return cnt

def BFS(sr, sc):
    global cnt

    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if arr[r][c] == 0 and arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    visited[nr][nc] = 1
                else:
                    visited[nr][nc] = 1
                    q.append((nr, nc))


arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cnt = 0
last = now_cheese(arr)
while True:
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    BFS(0, 0)
    now = now_cheese(arr)
    cnt += 1
    if now:
        last = now
    else:
        print(cnt)
        print(last)
        break
