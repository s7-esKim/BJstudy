from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(a, b):
    global count
    q = deque([(a, b)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    q.append((nx, ny))
    count += 1
    return


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    count = 0

    for k in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
    print(count)
