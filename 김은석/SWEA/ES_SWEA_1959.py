T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input(). split()))
    B = list(map(int, input(). split()))
    if N > M:
        N, M = M, N
        A, B = B, A
    result = -999999999999999
    for i in range(M-N+1):
        max_value = 0
        for j in range(N):
            max_value += A[j] * B[j+i]
        if max_value > result:
            result = max_value
    print(f'#{tc} {result}')


