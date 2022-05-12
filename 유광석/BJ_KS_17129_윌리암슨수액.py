from collections import deque

def check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                return (i, j)

def BFS(sr, sc):
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1 and visited[nr][nc] == -1 :
                if arr[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                
                elif arr[nr][nc] > 2:
                    print('TAK')
                    print(visited[r][c] + 1)
                    return
    print('NIE')
    return
        

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

i, j = check()
visited[i][j] = 0
BFS(i, j)
