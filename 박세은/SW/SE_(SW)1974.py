import sys
sys.stdin = open('input.txt')


def row_search(arr):
    for i in arr:
        for j in range(len(arr)-1):
            for k in range(j+1, len(arr)):
                if i[j] == i[k]:
                    return 0
    else:
        return 1


def column_search(arr):
    col_arr = []
    for i in range(len(arr)):
        a = [arr[j][i] for j in range(len(arr))]
        col_arr.append(a)

    for i in col_arr:
        for j in range(len(col_arr)-1):
            for k in range(j+1, len(col_arr)):
                if i[j] == i[k]:
                    return 0
    else:
        return 1


def square_search(arr):
    square_arr = []
    for i in range(0, 9, 3):
        for k in range(0, 9, 3):

            a = []
            for j in range(3):
                for l in range(3):
                    a.append(arr[j+i][l+k])
            square_arr.append(a)

    for i in square_arr:
        for j in range(len(square_arr)-1):
            for k in range(j+1, len(square_arr)):
                if i[j] == i[k]:
                    return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if row_search(arr) == 1 and column_search(arr) == 1 and square_search(arr) == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

