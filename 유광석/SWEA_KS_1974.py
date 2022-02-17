import sys
sys.stdin = open('input (4).txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]       # 정 방향
    arr_c = [[0]*9 for i in range(9)]                               # 횡 방향
    arr_sq = []                                                     # 사각형 모양

    for i in range(9):                                              # 전치!
        for j in range(9):
            arr_c[i][j] = arr[j][i]
    # 델타로 팔방 값을 확인해줌
    dx = [-1, 0, 1 , -1, 0, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    for x, y in [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]:
        empty_list = []
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            empty_list.append(arr[ny][nx])
        arr_sq.append(empty_list)

    total = arr + arr_c + arr_sq            # 리스트를 한데 모아서

    for i in total:                         # 하나씩 돌면서 set으로 9가 아니면 0출력
        if len(set(i)) != 9:
            print(f'#{tc} {0}')
            break
    else:
        print(f'#{tc} {1}')                 # 아니면 for - else 로 1 출력