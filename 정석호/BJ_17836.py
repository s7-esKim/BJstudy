'''
3 3 7
0 2 1
1 1 1
1 1 0
'''

from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))   # 상하좌우

def bfs():
    q = deque()
    q.append((0,0))
    v[0][0] = 1
    knife = 100000
    while q:
        ci, cj = q.popleft()

        # 검을 만난다면 현재위치에서 공주님 위치까지의 최단 거리 더하기
        if arr[ci][cj] == 2:
            knife = v[ci][cj]-1 + abs(N-ci-1) + abs(M-cj-1)

        # 공주님 위치에 도착한다면 검을 가졌을 때와 그냥 갔을 때의 최솟값 리턴
        if (ci == N-1) and (cj == M-1):
            return min(knife, v[ci][cj]-1)

        # 이동할 수 있는 4방향 탐색
        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                if arr[ni][nj] == 0 or arr[ni][nj] == 2:
                    v[ni][nj] = v[ci][cj] + 1  # 다음위치 값 = 현재위치의 값 + 1
                    q.append((ni,nj))

    return knife

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
result = bfs()

if result > T:      # 시간 안에 구출하지 못하면 fail
    print('Fail')
else:
    print(result)
