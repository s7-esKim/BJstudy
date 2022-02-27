import sys
sys.stdin = open('input.txt')


def max_multi(A, B, len_A, len_B):  # len_A < len_B
    max_ab = 0
    start = 0
    while start != len_B-len_A+1:  # A = 3, B = 5 -> B[2] 까지만 이동 : B[3] 부터 실행 X
        sum_mul = 0
        for i in range(len_A):
            mul = A[i] * B[i + start]  # 마주보는 두 수 곱하기
            sum_mul += mul  # 곱한 수를 sum_mul에 더해주기
        if sum_mul > max_ab:
            max_ab = sum_mul
        start += 1
    return max_ab


T = int(input())
for tc in range(1, T+1):
    len_A, len_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = 0
    if len_A < len_B:
        answer = max_multi(A, B, len_A, len_B)
    else:
        answer = max_multi(B, A, len_B, len_A)

    print(f'#{tc} {answer}')
