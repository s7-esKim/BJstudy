import sys
sys.stdin = open('input 2001.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    big_arr = []
    for i in range(N):
        arr = list(map(int, input().split()))
        big_arr.append(arr)

    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            dead_sum = 0
            for k in range(M):
                for l in range(M):
                    dead_sum += big_arr[k+i][l+j]

            if max_num < dead_sum:
                max_num = dead_sum

    print(f'#{tc} {max_num}')
