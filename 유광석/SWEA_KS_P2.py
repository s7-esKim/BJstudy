import sys
sys.stdin = open('in1_2.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for k in range(1, M + 1):
        if M % k == 0:
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if arr[i-1][j-1] == 0:
                        arr[i-1][j-1] = 1
                    else:
                        arr[i-1][j-1] = 0

        else:
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if (i+j) % k == 0:
                        if arr[i-1][j-1] == 0:
                            arr[i-1][j-1] = 1
                        else:
                            arr[i-1][j-1] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt += 1

    print(f'#{tc} {cnt}')