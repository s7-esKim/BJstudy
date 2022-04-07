import sys
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def BFS(i, j):
    global min_v
    
    q = deque()
    q.append((i, j, 0))
    visited[i][j][0] = 1 

    while q:
        r, c, w = q.popleft()

        if r == N - 1 and c == M - 1:
            print(visited)
            if min_v > visited[r][c][w]:
                min_v = visited[r][c][w]
                return

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == '1' and w == 0:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    q.append((nr, nc, 1))

                elif arr[nr][nc] == '0' and visited[nr][nc][w] == 0:
                    visited[nr][nc][w] = visited[r][c][w] + 1
                    q.append((nr, nc, w))
                    
                    

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
min_v = 2<<63-1
BFS(0, 0)

if min_v == 2<<63-1:
    print(-1)
else:
    print(min_v)