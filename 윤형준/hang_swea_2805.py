import sys
sys.stdin = open('input 2805.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    my_sum = 0

    arr = [list(map(int,input())) for _ in range(N)]
    for i in range(N//2+1):
        for j in range(N//2-i, N//2+1+i):
            if i ==  N//2:
                my_sum += arr[i][j]
            else:
                my_sum += arr[i][j]
                my_sum += arr[N-1-i][j]

    print(f'#{tc} {my_sum}')