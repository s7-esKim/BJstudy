import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    arr90 = [[0] * N for _ in range(N)]
    arr180 = [[0] * N for _ in range(N)]
    arr270 = [[0]* N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr90[i][j] = arr[N-1-j][i]
            arr180[i][j] = arr[N-1-i][N-1-j]
            arr270[i][j] = arr[j][N-1-i]

    print(f'#{tc}')
    for a1, a2, a3 in zip(arr90, arr180, arr270):
        print(f'{"".join(map(str, a1))} {"".join(map(str, a2))} {"".join(map(str, a3))}')
