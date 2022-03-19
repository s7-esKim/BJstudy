N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
queue = [(0,0)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1

while queue:
    ci, cj = queue.pop(0)

    for di, dj in ((-1,0),(1,0),( 0,-1),(0,1)):
        ni = ci + di
        nj = cj + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            visited[ni][nj] = visited[ci][cj] + 1
            queue.append((ni, nj))

print(visited[N-1][M-1])