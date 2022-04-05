import sys
sys.stdin = open('1.txt')
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[i][j] = 1
    color = arr[i][j]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] == color:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    bfs(nx, ny)


n = int(input())
arr = [list(input())for _ in range(n)]
visited = [[0] * n for _ in range(n)]


non_blind, blind = 0, 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            non_blind += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            blind += 1

print(non_blind, blind)