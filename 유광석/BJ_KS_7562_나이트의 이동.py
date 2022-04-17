from collections import deque

dr = (-2, -1, 1, 2, 2, 1, -1, -2)
dc = (-1, -2, -2, -1, 1, 2, 2, 1)

N = int(input())
for tc in range(N):
    I = int(input())
    sr, sc = map(int, input().split())
    tr, tc = map(int, input().split())
    visited = [[0]*I for _ in range(I)]
    q = deque()
    visited[sr][sc] = 1
    q.append((sr, sc))

    while q:
        r, c = q.popleft()

        if r == tr and c == tc:
            print(visited[tr][tc]-1)
            break

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))



