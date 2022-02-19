T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rotate90 = [[0] * N for _ in range(N)]
    rotate180 = [[0] * N for _ in range(N)]
    rotate270 = [[0] * N for _ in range(N)]

    # 90도
    for i in range(N):
        for j in range(N):
            rotate90[i][j] = arr[N-j-1][i]

    # 180도
    for i in range(N):
        for j in range(N):
            rotate180[i][j] = rotate90[N-j-1][i]

    # 270도
    for i in range(N):
        for j in range(N):
            rotate270[i][j] = rotate180[N-j-1][i]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(rotate90[i][j], end = '')
        print(end = ' ')
        for k in range(N):
            print(rotate180[i][k], end = '')
        print(end=' ')
        for l in range(N):
            print(rotate270[i][l], end='')
        print()
