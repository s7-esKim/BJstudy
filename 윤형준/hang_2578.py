def check_bingo(lst):
    cnt = 0
    diagonal_sum = 0
    diagonal_sum2 = 0
    for i in range(5):
        row_sum = 0
        col_sum = 0
        for j in range(5):
            row_sum += lst[i][j]
            col_sum += lst[j][i]
            if i == j:
                diagonal_sum += lst[i][j]
            if i+j == 4:
                diagonal_sum2 += lst[i][j]

        if row_sum == 0:
            cnt += 1
        if col_sum == 0:
            cnt += 1
    if diagonal_sum == 0:
        cnt += 1
    if diagonal_sum2 == 0:
        cnt += 1


    if cnt >= 3:
        return True
    else:
        return False

arr = [list(map(int, input().split())) for _ in range(5)]   # 내 빙고판

bingo_arr = [[1] * 5 for _ in range(5)]                     # 5 by 5 빙고 확인용

num = [list(map(int, input().split())) for _ in range(5)]   # 사회자가 부르는 수

cnt = 0

for k in range(5):

    for l in range(5):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == num[k][l]:
                    bingo_arr[i][j] = 0
                    cnt += 1
                    break

        if cnt >= 11 and check_bingo(bingo_arr):
            print(cnt)
            break
    if check_bingo(bingo_arr):
        break

# def check_bingo(lst):
#     cnt = 0
#     diagonal_sum = 0
#     diagonal_sum2 = 0
#     for i in range(5):
#         row_sum = 0
#         col_sum = 0
#         for j in range(5):
#             row_sum += lst[i][j]
#             col_sum += lst[j][i]
#             if i == j:
#                 diagonal_sum += lst[i][j]
#             if i+j == 4:
#                 diagonal_sum2 += lst[i][j]
#
#         if row_sum == 0:
#             cnt += 1
#         if col_sum == 0:
#             cnt += 1
#     if diagonal_sum == 0:
#         cnt += 1
#         # diagonal_sum = 1
#     if diagonal_sum2 == 0:
#         cnt += 1
#         # diagonalsum2 = 1
#
#     if cnt >= 3:
#         return True
#     else:
#         return False
#
# arr = [list(map(int, input().split())) for _ in range(5)]   # 내 빙고판
#
# bingoarr = [[1] * 5 for _ in range(5)]                     # 5 by 5 빙고 확인용
#
# num = [list(map(int, input().split())) for _ in range(5)]   # 사회자가 부르는 수
#
# cnt = 0
# for k in range(5):
#     for l in range(5):
#         for i in range(5):
#             for j in range(5):
#                 if arr[i][j] == num[k][l]:
#                     bingoarr[i][j] = 0
#                     cnt += 1
#                     break
#
#         if cnt >= 11 and check_bingo(bingoarr):
#             print(cnt)
#             break
#     if check_bingo(bingoarr):
#         break