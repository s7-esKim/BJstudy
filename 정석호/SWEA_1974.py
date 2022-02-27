import sys
sys.stdin = open('input.txt')

def checksudoku(arr):
    for i in range(9):
        low = [0] * 9
        for j in range(9):
            low[arr[i][j] - 1] += 1
        for k in low:
            if k != 1:
                return 0

    for i in range(9):
        column = [0] * 9
        for j in range(9):
            column[arr[j][i] - 1] += 1
        for k in column:
            if k != 1:
                return 0

    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            box = [0] * 9
            for k in range(3):
                for l in range(3):
                    box[arr[i + k][j + l] - 1] += 1
            for x in box:
                if x > 1:
                    return 0

    return 1

T = int(input())
for tc in range(1, T + 1):
    boxes = [list(map(int, input().split())) for _ in range(9)]
    result = checksudoku(boxes)

    print(f'#{tc} {result}')

