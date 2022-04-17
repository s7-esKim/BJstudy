from collections import deque
import sys

N, L, R = map(int, input().split())

def make_union(r, c):
    global avg

    avg += arr[r][c]
    population = []
    population.append((r, c))
    visited[r][c] = 1
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()
        print(q)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N and L <= abs(arr[nr][nc] - arr[r][c]) <= R and not visited[nr][nc]:
                visited[nr][nc] = 1
                avg += arr[nr][nc]
                q.append((nr, nc))
                population.append((nr, nc))
    avg //= len(population)
    return population

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
new_arr = [i[:] for i in arr]
cnt = 0

while True:
    cnt += 1
    visited = [[0]*N for _ in range(N)]
    avg = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                a = make_union(i, j)
                if a:
                    for r, c in a:
                        arr[r][c] = avg
            avg = 0

    if arr == new_arr:
        break
    else:
        new_arr = [i[:] for i in arr]

print(cnt-1)