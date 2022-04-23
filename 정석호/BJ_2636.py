from collections import deque

di, dj = ((-1,1,0,0), (0,0,-1,1))   # 상하좌우

def bfs():
    q = deque()
    # 초기 값 설정
    q.append((0,0))
    v[0][0] = 1
    cheese = 0

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0<= ni < N and 0<= nj < M and not v[ni][nj]:
                # 공기를 만나면 방문체크와 q 리스트에 추가
                if arr[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))
                # 아직 치즈이면 방문체크와 cheese 갯수 추가
                elif arr[ni][nj] == 1:
                    v[ni][nj] = 1
                    arr[ni][nj] = 0
                    cheese += 1
    return cheese

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [] # 시간마다 치즈의 갯수를 추출할 리스트
time = 0    # 시간 초기값
while True:
    time += 1
    v = [[0] * M for _ in range(N)]     #방문 체크용 리스트
    cnt = bfs()
    result.append(cnt)  # 한 시간의 치즈 갯수 추가
    if cnt == 0:        # 치즈가 없으면 break
        break

print(time-1)           # 시간 출력
print(result[-2])       # 한 시간 전의 치즈 갯수 출력