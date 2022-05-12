from collections import deque

di, dj = ((-1,1,0,0) , (0,0,-1,1))  # 상하좌우

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            # 다음 위치가 범위 내에 있고 장애물이 아니고 방문한 적이 없을 때
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 1 and not v[ni][nj]:
                # 빈 복도일 때
                if arr[ni][nj] == 0:
                    v[ni][nj] = v[ci][cj] + 1   # 다음위치 = 현재위치 + 1
                    q.append((ni,nj))   # q리스트에 추가
                # 청국장, 스시, 맥앤치즈를 만났을 때는 바로 리턴
                else:
                    return v[ci][cj]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

result = 0      # 최단 거리 값
# 시작 위치 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            result = bfs(i, j)
            break

# 최단 거리 값이 있을 때
if result:
    print('TAK')
    print(result)
# 음식을 먹을 수 없을 때
else:
    print('NIE')
