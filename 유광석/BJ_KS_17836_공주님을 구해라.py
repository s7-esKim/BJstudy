from collections import deque
import sys

def BFS(r, c, gram):
    q = deque()
    q.append((r, c, gram))

    while q:
        r, c, gram = q.popleft()

        if gram:
            if visited[r][c] > T:
                print('Fail')
                return
        else:
            if arr[r][c] > T:
                print('Fail')
                return
                
        if r == N -1 and c == M - 1:
            if gram:
                print(visited[r][c])
                return
            else:
                print(arr[r][c])
                return

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if gram:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] +1
                        q.append((nr, nc, True))

                else:
                    if arr[nr][nc] == '0':
                        arr[nr][nc] = arr[r][c] + 1
                        q.append((nr, nc, False))

                    elif arr[nr][nc] == '2':
                        arr[nr][nc] = arr[r][c] + 1
                        visited[r][c] = arr[r][c]
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc, True))

    print('Fail')
    return

N, M, T = map(int, input().split())
arr = [list(sys.stdin.readline().strip().split()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
if arr[0][0] == '2':
    arr[0][0] = 0
    BFS(0, 0, True)
else:
    arr[0][0] = 0
    BFS(0, 0, False)
