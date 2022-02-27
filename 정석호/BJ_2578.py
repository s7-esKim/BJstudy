def bingo_3(lst):
    total = 0 # 빙고 초기값
    # 가로줄 빙고 확인
    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[i][j] == 0:
                cnt += 1
        if cnt == 5:
            total += 1

    # 세로줄 빙고 확인
    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[j][i] == 0:
                cnt += 1
        if cnt == 5:
            total += 1

    # 왼쪽 대각선 빙고 화인
    cnt = 0
    for i in range(5):
        if lst[i][i] == 0:
            cnt += 1
    if cnt == 5:
        total += 1

    # 오른쪽 대각선 빙고 확인
    cnt = 0
    for i in range(5):
        if lst[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        total += 1

    return total

bingo = [list(map(int, input().split())) for _ in range(5)] # 빙고 판 생성
check_lst = [] #사회자 부르는 값 생성
for i in range(5):
    check = list(map(int, input().split()))
    check_lst.extend(check)

bingo_cnt = 0
for i in check_lst:
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == i:
                bingo[j][k] = 0
                bingo_cnt += 1
    BINGO = bingo_3(bingo)
    if BINGO >= 3:
        print(bingo_cnt)
        break



