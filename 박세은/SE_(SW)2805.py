import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    sum_arr = 0  # 수익
    center = N//2  # 가운데 index
    a = 1
    for j in range(center+1):  # 가운데를 기준으로 계산
        if j == 0:  # 한 가운데 일 경우 모든 행 더하기
            for k in range(N):
                sum_arr += arr[center][k]
        else:
            # 열 : center-1, center+1 / -2, +2 / ... / -center, +center (0, N-1)
            # 행 : 1 ~ N-1 / 2 ~ N-2 / ...
            for k in range(a, N-a):
                sum_arr += arr[center - j][k]
                sum_arr += arr[center + j][k]
            a += 1

    print(f'#{tc} {sum_arr}')