import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(a, b):
    q = deque([(a, b)])
    country = [(a, b)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and move[nx][ny] == 0:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    move[nx][ny] = 1
                    q.append((nx, ny))
                    country.append((nx, ny))
    return country


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
MOVE = True
while MOVE:
    move = [[0]*N for _ in range(N)]
    MOVE = False
    for i in range(N):
        for j in range(N):
            if move[i][j] == 0:
                move[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    MOVE = True
                    people = sum(arr[x][y] for x, y in country) // len(country)
                    for x, y in country:
                        arr[x][y] = people
    if answer > 2001:
        answer = 2001
        break
    if not MOVE:
        break
    answer += 1

print(answer)