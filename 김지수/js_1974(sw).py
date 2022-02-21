import sys

sys.stdin = open('새 텍스트 문서.txt')


def bubble(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 가로세로검증
    total = 1
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(arr)):
        row = []
        column = []
        for j in range(len(arr)):
            row.append(arr[i][j])
            column.append(arr[j][i])
        bubble_row = bubble(row)
        bubble_column = bubble(column)
        if bubble_row != num or bubble_column != num:
            total = 0

        # 사각형검증
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            square = []
            for i2 in range(3):
                for j2 in range(3):
                    square.append(arr[i + i2][j + j2])
            bubble_square = bubble(square)
            if bubble_square != num:
                total = 0

    print(f'#{tc} {total}')