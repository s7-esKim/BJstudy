import sys
sys.stdin = open('input (3).txt')

def new_arr(arr):
    return [i[:] for i in arr]

def sort(arr):
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j] # 0 1 1 0
    return arr

def make_str(arr, board, n):
    for i in range(N):
        board[i][n] += ''.join(arr[i])
    return board

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_ans = [['' for i in range(N)]for i in range(N)]


    arr_90 = new_arr(arr)
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N - 1 - i][j]


    arr_180 = new_arr(arr)
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr[N-1-i][N-1-j]

    arr_270 = new_arr(arr)
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr[i][N-1-j]

    d90 = make_str(sort(arr_90), arr_ans, 0)
    d180 = make_str(arr_180, d90, 1)
    d270 = make_str(sort(arr_270), d180, 2)

    print(f'#{tc}')
    for i in d270:
        print(' '.join(i))