def BFS(q):

    while q:
        r, c = q.pop(0)

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bs = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bs.append((i, j))

BFS(bs)

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > ans:
            ans = arr[i][j]

print(max(map(max, arr))-1)
# print(ans-1)

