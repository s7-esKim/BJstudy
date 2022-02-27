import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]
            arr_180[i][j] = arr[N-1-i][N-1-j]
            arr_270[i][j] = arr[j][N-1-i]

    print(f'#{tc}')
    for a1, a2, a3 in zip(arr_90, arr_180, arr_270):
        print(f'{"".join(map(str, a1))} {"".join(map(str, a2))} {"".join(map(str, a3))}')

