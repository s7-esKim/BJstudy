from collections import deque

di, dj = ((-1,1,0,0,1,1,-1,-1), (0,0,-1,1,1,-1,-1,1))

def bfs(x,y):
    q = deque()
    v = [[0]*M for _ in range(N)]   # 방문 리스트
    q.append((x,y))
    v[x][y] = 1

    while q:
        si, sj = q.popleft()
        # 상어를 만나면 안전거리 값 리턴
        if arr[si][sj] == 1:
            return v[si][sj]-1
        # 상하좌우 대각선 순회
        for i in range(8):
            ni, nj = si+di[i], sj+dj[i]
            if 0<=ni<N and 0<=nj<M and not v[ni][nj]:
                v[ni][nj] = v[si][sj] + 1   # 다음위치 = 현재위치 + 1
                q.append((ni,nj))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
# 모든 위치 순회
for i in range(N):
    for j in range(M):
        cnt = bfs(i,j)      # 안전거리 값
        # 안전거리 최댓값 구하기
        if result < cnt:
            result = cnt

print(result)

