import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dic = {'A': 2, 'B': 3, 'C': 4}

    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            # 공터도 아니고 집도 아닌 경우 == 기지국인 경우
            if arr[i][j] != 'X' and arr[i][j] != 'H':
                for k in range(1, dic[arr[i][j]]):
                    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        ni, nj = i+di*k, j+dj*k
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')