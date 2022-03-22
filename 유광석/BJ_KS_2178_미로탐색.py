from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

def bfs(c, r):
    queue = deque()
    queue.append((c, r))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        c, r = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nc < N and 0 <= nr < M and arr[nc][nr] == 1:
                arr[nc][nr] = arr[c][r] + 1
                queue.append((nc, nr))

bfs(0, 0)

print(arr[N-1][M-1])