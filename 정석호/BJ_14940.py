from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))   #상하좌우

def bfs():
    q = deque()
    q.append((s,e))
    v[s][e] = 1
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:   # 범위 안에 있고 방문하지 않았을 때
                if arr[ni][nj]:     # 갈 수 있는 땅일 때
                    v[ni][nj] = 1
                    arr[ni][nj] = arr[ci][cj] + 1
                    q.append((ni,nj))

    # 갈 수 있는 땅이지만 도달 할 수 없는 땅
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not v[i][j]:
                arr[i][j] = -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

# 목표 지점 찾기
s = e = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            arr[i][j] = 0
            s,e = i,j

bfs()

for i in arr:
    print(*i)