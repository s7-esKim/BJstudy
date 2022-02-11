import sys
sys.stdin = open('input.txt')

T = int(input())
for ts in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        fa = list(map(int, input().split()))
        arr[i] = fa

    max_v = 0
    for a in range(N - M + 1):
        for b in range(N - M + 1):
            sum_v = 0
            for j in range(M):
                for k in range(M):
                    sum_v += arr[a+j][b+k]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{ts} {max_v}')