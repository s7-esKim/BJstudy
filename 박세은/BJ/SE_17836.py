import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs():
    global answer
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if arr[x][y] == 2:
            answer = (N-1-x) + (M-1-y) + (visited[x][y]-1)
        if x == N-1 and y == M-1:
            return min(visited[x][y]-1, answer)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return answer


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 10001

answer = bfs()
if answer > T:
    print('Fail')
else:
    print(answer)