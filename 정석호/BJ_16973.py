from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))

# 직사각형 넓이에서 벽이 있는지 판별
def wall(x, y):
    v[x][y] = 1
    for i,j in walls:
        if x <= i < x+H and y <= j < y+W:
            return False
    return True

def bfs():
    q = deque()
    q.append((sx-1, sy-1))
    v[sx-1][sy-1] = 1

    while q:
        ci, cj = q.popleft()
        # 도착 지점에 도달했을 때
        if ci == ex-1 and cj == ey-1:
            return v[ci][cj] - 1

        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0<=ni<=N-H and 0<=nj<=M-W:   # 다음 위치가 직사각형 넓이를 뺸 범위 내에 있을 때
                if not v[ni][nj] and wall(ni, nj):  # 방문 하지 않았고 직사각형 넓이에 벽이 없을 때
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni,nj))
    return -1   # 도착 지점에 가지 못했을 때

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

# 벽이 있는 좌표 찾기
walls = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            walls.append([i,j])

# 직사각형 세로 길이, 직사각형 가로 길이, 처음 x좌표, 처음 y좌표, 도착 x좌표, 도착 y좌표
H, W, sx, sy, ex, ey = map(int, input().split())
print(bfs())