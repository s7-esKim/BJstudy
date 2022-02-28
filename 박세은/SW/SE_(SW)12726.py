import sys
sys.stdin = open('in1.txt')


def toggle(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                arr[i][j] = 0
            else:
                arr[i][j] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, M+1):
        if M % i == 0:
            toggle(arr)
        else:
            for x in range(N):
                for y in range(N):
                    if (x+y+2) % i == 0:
                        if arr[x][y] == 1:
                            arr[x][y] = 0
                        else:
                            arr[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
    print(f'#{tc} {count}')
