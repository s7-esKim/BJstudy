# 북(0), 서(1), 남(2), 동(3)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def robot(x, y, d):
    global count
    # 1으로 들어온 경우 동쪽 -> 3
    # 3으로 들어온 경우 서쪽 -> 1
    if d == 1:
        d = 3
    elif d == 3:
        d = 1

    arr[x][y] = 2  # 청소한 곳 표시
    count += 1     # 청소한 칸의 개수
    while True:
        num = 0
        # 4번 까지만 실행
        while num < 4:
            d = (d+1) % 4   # 왼쪽으로 회전
            num += 1        # 실행 횟수 증가
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:  # 청소를 하지 않는 칸이라면
                    arr[nx][ny] = 2   # 청소한 곳으로 표시
                    count += 1        # 청소한 칸의 개수 +1
                    # 청소한 칸으로 이동
                    x = nx
                    y = ny
                    # 실행 횟수 초기화
                    num = 0
        # 현재 바라보는 방향을 기준으로 뒤쪽으로 이동
        nd = (d+2) % 4
        x = x + dx[nd]
        y = y + dy[nd]
        # 뒤쪽이 벽이라면 종료
        if arr[x][y] == 1:
            return count


N, M = map(int, input().split())
i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0
robot(i, j, d)
print(count)