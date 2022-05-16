def walls_falling(q):

    while q:
        r, c, cnt = q.pop(0)
        if 0 <= r + 1 < 8:
            visited[r+1][c][cnt+1] = '#'
            q.append((r+1, c, cnt+1))


def BFS(sr, sc):
    q = []
    q.append((sr, sc, 0))

    while q:
        r, c, cnt = q.pop(0)
        if cnt >= 7:
            return 1

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][cnt] != '#' and visited[nr][nc][cnt+1] == '.':
                visited[nr][nc][cnt+1] = 1
                q.append((nr, nc, cnt+1))

    return 0

N = M = 8
arr = [list(input()) for _ in range(M)]
visited = [[['.'] * 8 for _ in range(8)] for _ in range(8)]
walls = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            visited[i][j][0] = '#'
            walls.append((i, j, 0))
walls_falling(walls)

ans = BFS(7, 0)
print(ans)
