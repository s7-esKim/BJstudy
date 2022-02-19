import sys
sys.stdin = open('input 1959.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    arrN = list(map(int,input().split()))

    arrM = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        arrN, arrM = arrM, arrN
    max_sum = 0

    for i in range(M-N+1):
        product_sum = 0
        for j in range(N):
            product_sum += arrN[j] * arrM[i+j]
        if max_sum < product_sum:
            max_sum = product_sum

    print(f'#{tc} {max_sum}')
