from collections import deque
# 나이트 이동 경로 생성
di, dj = ((-2,-2,2,2,-1,1,-1,1),(-1,1,-1,1,2,2,-2,-2))

def bfs():
    q = deque()
    q.append((sx,sy))
    chess[sx][sy] = 1   # 시작 좌표 값
    # 시작좌표와 도착좌표가 같으면 바로 리턴
    if sx == ex and sy == ey:
        return 0
    while q:
        ci, cj = q.popleft()
        for i in range(8):
            ni, nj = ci+di[i], cj+dj[i]     # 다음 좌표
            if 0 <= ni < N and 0 <= nj < N and not chess[ni][nj]:   # 범위 안에 있을 떄
                chess[ni][nj] = chess[ci][cj] + 1   
                # 도착좌표에 도착했을때 리턴
                if ni == ex and nj == ey:
                    return chess[ni][nj]-1
                q.append((ni,nj))

T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())      # 시작 좌표 x, 시작 좌표 y
    ex, ey = map(int, input().split())      # 도착 좌표 x, 도착 좌표 y
    chess = [[0] * N for _ in range(N)]     # 체스판 생성
    print(bfs())