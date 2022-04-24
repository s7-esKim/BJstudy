from collections import deque

even_d = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0))
odd_d = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1))

M, N = map(int, input().split())

arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]

q = deque()
q.append((0, 0))
arr[0][0] = -1
while q:
    r, c = q.popleft()

    if r % 2:
        for dr, dc in odd_d:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 0:
                arr[nr][nc] = -1
                q.append((nr, nc))
    else:
        for dr, dc in even_d:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 0:
                arr[nr][nc] = -1
                q.append((nr, nc))
cnt = 0

visited = [[0] * (M+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(M+2):
        if arr[i][j] == 1 and visited[i][j] == 0:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                r, c = q.popleft()

                if r % 2:
                    for dr, dc in odd_d:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                        
                        elif visited[nr][nc] == 0 and arr[nr][nc] == -1:
                            cnt += 1
                
                else:
                    for dr, dc in even_d:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 1 and  visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))

                        elif visited[nr][nc] == 0 and arr[nr][nc] == -1:
                            cnt += 1
                

print(cnt)
