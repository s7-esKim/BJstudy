dir = [[-1,0], [0,1], [1,0], [0,-1]]    # 북동남서 방향
# left = [3,0,1,2]
N, M = map(int, input().split())
r, c, d = map(int, input().split())     # 처음 x, 처음 y, 방향
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

v[r][c] = 1
cnt = 0
while True:
    temp = 0    # 네 방향 중 한번이라도 청소했는지 여부 판단
    # 네방향 순회
    for _ in range(4):
        left_x = r + dir[(d+3)%4][0]    # 왼쪽 회전 x 좌표
        left_y = c + dir[(d+3)%4][1]    # 왼쪽 회전 y 좌표
        d = (d+3)%4 # (0,3,2,1) 순서로 돌아야함
        if 0 <= left_x < N and 0 <= left_y < M and arr[left_x][left_y] == 0:
            if v[left_x][left_y] == 0:
                v[left_x][left_y] = 1
                r = left_x
                c = left_y
                temp = 1
                break

    if temp == 0:
        # 뒤에가 벽이면 종료
        if arr[r-dir[d][0]][c-dir[d][1]] == 1:
            for i in range(N):
                for j in range(M):
                    if v[i][j] == 1:
                        cnt += 1
            break
        # 벽이 아니면 후진
        else:
            r, c = r-dir[d][0], c-dir[d][1]
print(cnt)



di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
def bfs(si, sj):
    global d

    q = []
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        flag = 0
        ci, cj = q.pop()
        for idx in range(4):
            ni = ci + di[(d+1+idx)%4]
            nj = cj + dj[(d+1+idx)%4]
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
                d = (d+1+idx)%4
                flag = 1
                break
        if flag == 0:
            ni = ci - di[d]
            nj = cj - dj[d]
            if arr[ni][nj] != 1: # 벽이 아니면
                q.append((ni,nj))
            else:
                return

N, M = map(int, input().split())
si, sj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

bfs(si,sj)
print(sum(map(sum,v)))
