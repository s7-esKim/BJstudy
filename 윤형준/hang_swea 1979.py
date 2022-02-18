import sys
sys.stdin = open('input 1979.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)] # N by N 행렬

    result = 0 # K 길이의 단어가 들어갈 수 있는 수
    for i in range(N):
        row_cnt = 0 # 행 방향
        col_cnt = 0 # 열 방향
        for j in range(N):
            if arr[i][j]: # 1이면
                row_cnt += 1
            else: # 0이면
                if row_cnt == K: # 지금까지 쌓인 row_cnt가 K와 같으면 result += 1
                    result += 1
                row_cnt = 0

            if j == N-1 and row_cnt == K:
                result += 1

            if arr[j][i]:
                col_cnt += 1
            else:
                if col_cnt == K:
                    result += 1
                col_cnt = 0

            if j == N-1 and col_cnt == K:
                result += 1

    print(f'#{tc} {result}')