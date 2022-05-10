from collections import deque
import sys
input = sys.stdin.readline
# L 육지 W 바다


def BFS(sr, sc):
    global max_v

    cnt = 0
    q = deque()
    q.append((sr, sc, cnt))

    while q:
        r, c, cnt = q.popleft()

        if cnt > max_v:
            max_v = cnt

        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc, cnt+1))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_v = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            BFS(i, j)

print(max_v)



from collections import deque
import sys
input = sys.stdin.readline
# L 육지 W 바다

def BFS(sr, sc):
    global max_v

    cnt = 0
    q = deque()
    q.append((sr, sc, cnt))

    while q:
        r, c, cnt = q.popleft()

        if cnt > max_v:
            max_v = cnt

        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, cnt+1))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
root_set = set()
max_v = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L' and (i, j) not in root_set:
            tr=tc=False
            visited = set()
            visited.add((i, j))
            BFS(i, j)


print(max_v)