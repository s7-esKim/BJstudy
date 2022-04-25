import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = []
def bfs():
    q = deque([[0, 0]])
    visited[0][0] = 1
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visited[nx][ny] = 1
                    count += 1
    answer.append(count)
    return count


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    visited = [[0] * M for _ in range(N)]
    count = bfs()
    if count == 0:
        break
    time += 1
print(time)
print(answer[-2])