import sys
sys.stdin = open('1.txt')

def dfs(x, y, cnt):
    global total
    total = max(total, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and not visited[arr[ny][nx]]:
            visited[arr[ny][nx]] =  True
            dfs(nx, ny, cnt + 1)
            visited[arr[ny][nx]] = False


for tc in range(3):
    r, c = map(int, input().split())
    arr = [list(input()) for _ in range(r)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    total = 0
    visited = [False] * 26
    visited[arr[0][0]] = True
    dfs(0, 0, 1)
    print(total)