import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    M = N // 2 # 중간 인덱스 접근
    a = b = M
    total = 0
    for i in range(N):
        for j in range(a, b+1):
            total += arr[i][j]
        if i < M:
            a, b = a - 1, b + 1
        else:
            a, b = a + 1, b - 1

    print(f'#{tc} {total}')
