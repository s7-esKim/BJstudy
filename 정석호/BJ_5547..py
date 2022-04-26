from collections import deque

M, N = map(int, input().split())
arr = [[0]*(M+2) for _ in range(N+2)]
v = [[0]*(M+2) for _ in range(N+2)]
for i in range(1, N+1):
    arr[i][1:M+1] = map(int, input().split())

def bfs(y,x):
    q = deque()
    q.append((y,x))
    v[y][x] = 1
    cnt = 0
    while q:
        y, x = q.popleft()
        if y % 2:
            di, dj = ((0,1,1,0,-1,-1), (1,1,0,-1,0,1))
        else:
            di, dj = ((0,1,1,0,-1,-1), (1,0,-1,-1,-1,0))

        for i in range(6):
            ny, nx = y+di[i], x+dj[i]
            if 0 <= ny < N+2 and 0 <= nx < M+2:
                if arr[ny][nx] == 0 and not v[ny][nx]:
                    q.append((ny,nx))
                    v[ny][nx] = 1
                elif arr[ny][nx]:
                    cnt += 1
    return cnt

print(bfs(0,0))
