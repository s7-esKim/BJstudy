import sys
sys.setrecursionlimit(10**8)

di, dj = ((-1,1,0,0), (0,0,-1,1))   # 상하좌우

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[-1]*M for _ in range(N)]
def dfs(x, y):
    # 도착 지점에 오면 1 리턴
    if x == N-1 and y == M-1:
        return 1
    # 방문한 적이 있으면 그 위치에서 출발하는 경우의 수를 리턴
    if v[x][y] != -1:
        return v[x][y]
    v[x][y] = 0 # 방문 체크
    for i in range(4):
        ni, nj = x+di[i], y+dj[i]
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] < arr[x][y]: # 다음 위치가 현재위치보다 높이가 낮을 때
                v[x][y] += dfs(ni, nj)
    return v[x][y]
print(dfs(0,0))
