import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if c[x][y] != -1:
        return c[x][y]
    c[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if a[nx][ny] < a[x][y]:
                c[x][y] += dfs(nx, ny)
    return c[x][y]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
c = [[-1]*n for _ in range(m)]
print(dfs(0, 0))