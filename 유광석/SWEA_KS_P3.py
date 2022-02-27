import sys
sys.stdin = open('in1_3.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    di = [0, 0, -1, 1, -1, 1, -1, 1]
    dj = [-1, 1, 0, 0, -1, -1, 1, 1]

    for i in range(N):
        for j in range(N):
            for x in range(2):
                cnt = 0
                cnt += arr[i][j]
                for l in range(1, M):
                    for k in range(x * 4, 4 * (x + 1)):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            cnt += arr[ni][nj]

                if cnt > ans:
                    ans = cnt

    print(f'#{tc} {ans}')