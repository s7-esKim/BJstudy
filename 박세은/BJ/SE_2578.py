import sys
sys.stdin = open('input.txt')


def bingo(arr):
    count = 0
    # 행과 열에서 빙고 찾기
    for i in range(5):
        row = 0
        col = 0
        for j in range(5):
            row += arr[i][j]  # 행의 합
            col += arr[j][i]  # 열의 합
        # 열의 합이나 행의 합이 0인 경우 빙고 += 1
        if row == 0:
            count += 1
        if col == 0:
            count += 1
    # 대각선에서 빙고 찾기
    line1 = 0
    line2 = 0
    for i in range(5):
        line1 += arr[i][i]    # 오른쪽 대각선의 합
        line2 += arr[i][4-i]  # 왼쪽 대각선의 합
    # 오른쪽이나 왼쪽의 대각선의 합이 0인 경우 빙고 += 1
    if line1 == 0:
        count += 1
    if line2 == 0:
        count += 1

    return count


arr = [list(map(int, input().split())) for _ in range(5)]  # 철수의 빙고판
number = []                                                # 사회자가 부르는 숫자
for i in range(5):
    number += (list(map(int, input().split())))

count = 0
for n in range(len(number)):
    count += 1
    for x in range(5):
        for y in range(5):
            # 사회자가 부르는 숫자와 빙고판의 숫자가 같다면 그 값을 0 으로 바꿔준다
            if number[n] == arr[x][y]:
                arr[x][y] = 0
    # 값을 0으로 바꿔준 뒤에는 항상 빙고가 3개 만들어 졌는지 확인
    if bingo(arr) >= 3:
        break

print(count)
