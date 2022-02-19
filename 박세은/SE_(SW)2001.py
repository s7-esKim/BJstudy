import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 2차원 배열 만들기
    arr = [list(map(int, input().split())) for i in range(N)]

    max_die = 0  # 죽은 파리의 최대 개수
    # 1: arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1]
    for i in range(N-M+1):  # 0, 1, 2, 3
        for j in range(N-M+1):  # 0, 1, 2, 3
            die_fly = 0  # 죽은 파리의 개수
            for x in range(M):  # 0, 1
                for y in range(M):  # 0, 1
                    die_fly += arr[i+x][j+y]
            if max_die < die_fly:
                max_die = die_fly

    print(f'#{tc} {max_die}')