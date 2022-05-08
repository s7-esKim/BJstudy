'''
1
5 3
0 0 0 0 0
0 1 0 1 0
0 0 1 0 0
'''
from collections import deque

hi, hj = ((-2,-1,1,2,2,1,-1,-2), (1,2,2,1,-1,-2,-2,-1))     # 말의 이동
di, dj = ((-1,1,0,0), (0,0,-1,1))   # 상하좌우

def bfs():
    q = deque()
    q.append((0,0,0,K))     #x좌표, y좌표, 총 이동 수, 말 이동

    while q:
        ci, cj, cnt, horse = q.popleft()
        # 도착지점에 도달할 경우 총 이동 수 리턴
        if ci==N-1 and cj==M-1:
            return cnt

        # 말 이동이 가능할 때
        if horse >= 1:
            for i in range(8):
                ni, nj = ci+hi[i], cj+hj[i]
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:    # 범위 내에 있고 평지일 때
                    # 원숭이로 가다가 말로 가거나 , 말로 가다가 원숭이로 가는 것 중에 어떤 것이 최선일 지 모르기 때문에
                    # 다음 방문 위치가 말로 이동한 거리 -1 한 것보다 작다면 그 지점부터 다시 시작하게 한다.
                    if v[ni][nj] == -1 or v[ni][nj] < horse-1:  # 방문하지 않았고
                        v[ni][nj] = horse-1
                        q.append((ni,nj,cnt+1,horse-1))

        # 원숭이로 이동할 때
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:        # 범위 내에 있고 평지일 때
                # 1. 방문하지 않았거나
                # 2. 다음 위치가 말 이동보다 작을 때
                if v[ni][nj] == -1 or v[ni][nj] < horse:
                    v[ni][nj] = horse
                    q.append((ni,nj,cnt+1,horse))

    return -1   # 목적지에 도달할 수 없으면 -1


K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[-1]*M for _ in range(N)]      # 방문 체크

print(bfs())