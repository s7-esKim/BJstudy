# 1씩 증가 할 때마다 익은 토마토 상하좌우에 안익은 토마토가 익는걸로 바뀜
# 며칠이 지나면 토마토들이 다 익게 되는지에 대한 최소 일수
# 1, 0 -1 은 각각 익은 토마토, 익지 않은 토마토, 빈 곳
# bfs를 통해 0인부분 1로 바꾸기 도중에 -1,-1을 만나기전까지만
from collections import deque

def BFS(time):                                                                    # time: 우리가 찾아할 최소 일수
    while queue:
        time += 1
        for q in range(len(queue)):                                               # 꼭 익은 토마토가 1개라는 보장은 없음 (조건에 안주어짐)
            i, j = queue.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < M and 0 <= nj < N and tomato[ni][nj] == 0:
                    tomato[ni][nj] = 1
                    queue.append([ni, nj])
    return time

N, M = map(int, input().split())                                                    # N : 상자 세로  M : 상자 가로
tomato = [list(map(int, input().split())) for _ in range(M)]
queue = deque([])                                                                   # 큐 변수 생성
di = [0, 0, -1, 1]                                                                  # 왼, 오, 앞, 뒤  = 좌, 우, 상, 하
dj = [-1, 1, 0, 0]

for i in range(M):                                                                  # 익은 토마토 위치 찾기
    for j in range(N):
        if tomato[i][j] == 1:
            queue.append([i, j])

result = BFS(-1)
flag = True
for i in range(M):
    for j in range(N):
        if tomato[i][j] == 0:
            flag = False
            break

if flag:
    print(result)
else:
    print('-1')




