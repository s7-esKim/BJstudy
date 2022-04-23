di, dj = ((-1,1,0,0), (0,0,-1,1))   # 상하좌우

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for si in range(N):
    for sj in range(M):
        if arr[si][sj] == 'X':  # 지도에서 땅 찾기
            cnt = 0
            for i in range(4):  # 상하좌우 탐색
                ni, nj = si+di[i], sj+dj[i]
                # 다음 위치가 범위 밖이면 바다로 간주하므로 cnt에 1 더하기
                if ni < 0 or nj < 0 or ni >= N or nj >= M:
                    cnt += 1
                # 범위 내일 때 바다를 만나면 cnt에 1 더하기
                if 0<= ni <N and 0<= nj <M and arr[ni][nj] == '.':
                    cnt += 1
            # 상하좌우 탐색 후 바다가 3개 이상이면 '-1' 문자열로 바꿈
            if cnt >= 3:
                arr[si][sj] = '-1'

start_x = start_y  = 10 # 시작 좌표
end_x = end_y = 0       # 끝 좌표
for i in range(N):
    for j in range(M):
        # 땅일 때 최소와 최대의 x,y 좌표 찾기
        if arr[i][j] == 'X':
            if i < start_x:
                start_x = i
            if i > end_x:
                end_x = i
            if j < start_y:
                start_y = j
            if j > end_y:
                end_y = j

for i in range(start_x, end_x+1):
    for j in range(start_y, end_y+1):
        # '-1'을 '.'으로 바꿔줌
        if arr[i][j] == '-1':
            arr[i][j] = '.'
        print(arr[i][j], end='')
    print()