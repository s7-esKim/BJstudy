def bingo_check(lst):
    bingo_3 = 0
    # 가로줄
    for i in range(5):
        cnt = 0
        for j in range(5):
            if check[i][j] == 1:
                cnt += 1
        if cnt == 5:
            bingo_3 += 1
    #세로줄
    for i in range(5):
        cnt = 0
        for j in range(5):
            if check[j][i] == 1:
                cnt += 1
        if cnt == 5:
            bingo_3 += 1
    # 왼쪽 대각선
    cnt = 0
    for i in range(5):
        if check[i][i] == 1:
            cnt += 1
    if cnt == 5:
        bingo_3 += 1

    # 오른쪽 대각선
    cnt = 0
    for i in range(5):
        if check[i][4-i] == 1:
            cnt += 1
    if cnt == 5:
        bingo_3 += 1

    return bingo_3

arr = [list(map(int, input().split())) for _ in range(5)]
call = []
for i in range(5):
    call.extend(list(map(int, input().split())))
check = [[0]*5 for _ in range(5)]


call_cnt = 0
for c in call:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == c:
                call_cnt += 1
                check[i][j] = 1
    BINGO = bingo_check(check)
    if BINGO >= 3:
        print(call_cnt)
        break
