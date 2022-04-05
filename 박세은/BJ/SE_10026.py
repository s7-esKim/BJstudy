from collections import deque


def bfs(i, j, color, arr):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == color:
                q.append((nx, ny))
                arr[nx][ny] = 0


N = int(input())
arr1 = [list(map(str, input())) for _ in range(N)]
arr2 = [list([] for _ in range(N)) for _ in range(N)]
answer1 = answer2 = 0

# 적록색약이 보는 그림
for i in range(N):
    for j in range(N):
        if arr1[i][j] == 'R' or arr1[i][j] == 'G':
            arr2[i][j] = 'R'
        else:
            arr2[i][j] = 'B'

for i in range(N):
    for j in range(N):
        if arr1[i][j]:
            bfs(i, j, arr1[i][j], arr1)
            answer1 += 1
        if arr2[i][j]:
            bfs(i, j, arr2[i][j], arr2)
            answer2 += 1

print(answer1, answer2)
