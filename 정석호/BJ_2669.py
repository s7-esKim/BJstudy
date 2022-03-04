# BJ_2669 (직사각형 네개의 합집합의 면적 구하기)

# 문제 : 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

arr = [[0] * 101 for _ in range(101)]           # x좌표와 y좌표 2차원 행렬
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())  # x2-x1은 사각형의 가로 길이, y2-y1은 사각형의 세로 길이
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] += 1                      # 사각형의 넓이를 구하기 위해 행렬에 카운트

result = 0                                      # 사각형의 최종 넓이
for i in range(101):
    for j in range(101):
        if arr[i][j] != 0:
            result += 1                         # 행렬을 순회하면서 0이 아닌 순차적으로 더함.
print(result)
