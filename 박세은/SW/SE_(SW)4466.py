import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 시험을 친 과목 수, 선택하여 넣을 수 있는 과목 수
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 버블 정렬
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    arr_sum = arr[::-1]
    sum_arr = 0
    for i in range(K):
        sum_arr += arr_sum[i]
    print(f'#{tc} {sum_arr}')