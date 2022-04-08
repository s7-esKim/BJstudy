from collections import deque

def rotate(d):                                                    # 왼쪽 회전
    if d == 0:                                                    # 북쪽
        return 3                                                  # 서쪽
    elif d == 1:                                                  # 동쪽
        return 0                                                  # 북쪽
    elif d == 2:                                                  # 남쪽
        return 1                                                  # 동쪽
    elif d == 3:                                                  # 서쪽
        return 2                                                  # 남쪽

def bfs(i,j,direction):                                           # i,j: 시작위치 direction: 방향
    global cnt
    queue = deque([(i,j,direction)])
    arr[i][j] = -1                                                # 로봇 청소기가 있는 칸은 빈칸이므로 청소 가능
    cnt += 1                                                      # 횟수 1 증가

    while queue:
        ci, cj, d = queue.popleft()

        for i in range(4):
            d = rotate(d)                                          # a. 글 읽어보면 빈 공간이 존재하든 안하든 왼쪽회전은 변함없음
            ni = ci + di[d]                                        # 회전 후 다음 칸 전진
            nj = cj + dj[d]                                        # 회전 후 다음 칸 전진

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                queue.append((ni,nj,d))
                cnt += 1
                arr[ni][nj] = -1
                break                                               # BFS 개념이긴 하지만 로봇은 한개이므로 break문 쓰기

        else:                                                       # b. 4번 실행되고도 break를 못 만나면 else문 실행 할수 있도록 설정
            ni = ci - di[d]                                         # 후진 되는 경우
            nj = cj - dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:    # 벽이 아닌경우에만 후진 가능
                queue.append((ni,nj,d))


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1,0,1,0]
dj = [0,1,0,-1]

cnt = 0
bfs(r,c,d)
print(cnt)
