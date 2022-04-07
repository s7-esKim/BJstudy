from collections import deque
'''
1.현재 위치를 청소한다.
2.현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
    a.현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 
      그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
    b.1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
'''
def rotate(d): # 왼쪽 회전
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2

def bfs(i,j,direction): # i,j: 시작위치 direction: 방향
    global cnt
    queue = deque([(i,j,direction)])
    arr[i][j] = -1
    cnt += 1

    while queue:
        ci, cj, d = queue.popleft()

        for i in range(4):
            d = rotate(d)
            ni = ci + di[d]
            nj = cj + dj[d]

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                queue.append((ni,nj,d))
                cnt += 1
                arr[ni][nj] = -1
                break

        else:
            ni = ci - di[d]
            nj = cj - dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                queue.append((ni,nj,d))


N, M = map(int, input().split())
r, c, d = map(int, input().split()) # r,c는 로봇 좌표 d는 방향 0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1,0,1,0]
dj = [0,1,0,-1]

cnt = 0
bfs(r,c,d)
print(cnt)