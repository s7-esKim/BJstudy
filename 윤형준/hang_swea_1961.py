import sys
sys.stdin = open('input 1961.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[N-1-j][i], end='')
        print(' ', end='')
        for j in range(N):
            print(arr[N-1-i][N-1-j], end='')
        print(' ',end='')
        for j in range(N):
            print(arr[j][N-1-i], end='')
        print()
