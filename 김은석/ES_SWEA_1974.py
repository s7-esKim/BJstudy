def sudoku(arr):
    for i in range(9):
        row_list = []
        for j in range(9):
            if arr[i][j] in row_list:
                return 0
            row_list.append(arr[i][j])

    for i in range(9):
        column_list = []
        for j in range(9):
            if arr[j][i] in column_list:
                return 0
            column_list.append(arr[j][i])

    for i in range(0,9,3):
        for j in range(0,9,3):
            three_list = []

            for k in range(3):
                for l in range(3):
                    if arr[i+k][j+l] in three_list:
                        return 0
                    three_list.append(arr[i+k][j+l])

    return 1

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku(arr)

    print(f'#{tc} {result}')