'''
2개의 벽을 지우는 deletewall 함수를 이용하여
모든 조합의 경우를 다 조사한다.
deletwall 함수의 경우 재귀의 방식을 이용한 조합 함수이며
cnt == 2, 즉 2개의 벽이 제거되었으면
bfs 함수를 통해 미로의 도착 여부를 판단한다.
bfs 함수는 길(0)을 만날 때마다 이전 값에서 1을 더해준 값으로 계산했고
2에서 출발하여 도착지를 만날 때까지 3,4,5 ...식으로 커진다.
마지막 최종 도착지(3)을 만나면 금방 있던 check[ci][cj]를 리턴해주면 된다. (출발이 2니까)
maze를 복사한 check 배열을 만든 이유는 maze 함수 자체의 값을 바꿔버리면
deletewall에서 다음 벽을 조사할 때 이미 maze가 변해 있어서 새로운 check 배열을 만들어줬다.
'''
from collections import deque
import sys

def bfs():
    global result,flag
    queue = deque()
    queue.append((si,sj))
    check = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            check[i][j] = maze[i][j]
    while queue:
        ci, cj = queue.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M:
                if check[ni][nj] == 0:
                    check[ni][nj] = check[ci][cj] + 1
                    queue.append((ni,nj))
                if maze[ni][nj] == 3:
                    flag = 1
                    if result > check[ci][cj]:
                        result = check[ci][cj]
                        if result == N+M-1:
                            print(result)
                            exit()
                        return
'''
벽을 부술 수 있는 조합
cnt가 2, 즉 벽을 2개 허물었으면 bfs 함수 실행
'''
def deletewall(cnt):
    if cnt == 1:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                maze[i][j] = 0
                deletewall(cnt+1)
                maze[i][j] = 1

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
maze[0][0] = 2
maze[N-1][M-1] = 3
result = 123456789
'''
# flag 변수는 미로에서 도착지에 도달했으면 1로 바뀐다
모든 조합의 경우를 실행 후에도 flag가 0이라면
도착지에 도달하지 못했다는 뜻으로 마지막에 result를 -1로 바꿔준다
'''
flag = 0
# 출발지 si, sj
for i in range(N):
    for j in range(M):
        if maze[i][j] == 2:
            si, sj = i, j
deletewall(0)
if flag == 0:
    result = -1
print(result)
