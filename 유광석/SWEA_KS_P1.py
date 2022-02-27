import sys
sys.stdin = open('in1_4.txt')
import pprint

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 'H':
                            arr[ni][nj] = 'O'

            elif arr[i][j] == 'B':
                for l in range(2):
                    for k in range(4):
                        ni = i + di[k] * (1+l)
                        nj = j + dj[k] * (1+l)
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'O'

            elif arr[i][j] == 'C':
                for l in range(3):
                    for k in range(4):
                        ni = i + di[k] * (1+l)
                        nj = j + dj[k] * (1+l)
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'O'

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')


