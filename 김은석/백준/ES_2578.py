# 빙고게임
# 무조건 5 X 5
# 행 열 대각선
# 사회자가 하나씩 부를때마다 0으로 바꿈
# 사회자가 하나씩 부를때마다 행 열 대각선 비교해서 합이 0인 경우 선긋기
# 선 완성할때마다 +1
# 선이 3이 되는 순간에 빙고 즉 그때의 사회자가 부른 값 출력
def check(my_bingo):
    line = 0
    for x in range(5):
        count_row = 0
        for y in range(5):
            if my_bingo[x][y] == 0:
                count_row += 1
            if count_row == 5:
                line += 1

    for x in range(5):
        count_col = 0
        for y in range(5):
            if my_bingo[y][x] == 0:
                count_col += 1
            if count_col == 5:
                line += 1

    count_diagonal = 0
    count_reverse_diagonal = 0

    for x in range(5):
        if my_bingo[x][x] == 0:
            count_diagonal += 1
        if count_diagonal == 5:
            line += 1

        if my_bingo[4-x][x] == 0:
            count_reverse_diagonal += 1
        if count_reverse_diagonal == 5:
            line += 1

    return line


# def check(my_bingo):
#     line = 0
#     for a in range(5): # 행
#         total1 = 0
#         for b in range(5):
#             total1 += my_bingo[a][b]
#         if total1 == 0:
#             line += 1
#
#     for p in range(5): # 열
#         total2 = 0
#         for q in range(5):
#             total2 += my_bingo[q][p]
#         if total2 == 0:
#             line += 1
#
#     total3 = 0
#     for r in range(5): # 우상향 대각선
#         total3 += my_bingo[r][r]
#     if total3 == 0:
#         line += 1
#
#     total4 = 0
#     for r in range(5): # 우하향 대각선
#         total4 += my_bingo[r][4-r]
#     if total4 == 0:
#         line += 1
#
#     return line

my_bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call.extend(list(map(int, input().split())))

for i in range(25):
    for x in range(5):
        for y in range(5):
            if call[i] == my_bingo[x][y]:
                my_bingo[x][y] = 0
    if check(my_bingo) >= 3:
        print(i+1)
        break
