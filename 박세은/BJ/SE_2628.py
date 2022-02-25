# 0 <= X, Y <= 100, 가로/세로
X, Y = map(int, input().split())
N = int(input())
# 점선 -> 세로로 자르는 점선 : 가로 길이, 가로로 자르는 점선 : 세로 길이
x_line = [0, X]
y_line = [0, Y]
for i in range(N):
    a, b = map(int, input().split())
    if a:
        x_line.append(b)
    else:
        y_line.append(b)

# 오름차순 정렬
for i in range(len(x_line) - 1):
    min_i = i
    for j in range(i+1, len(x_line)):
        if x_line[min_i] > x_line[j]:
            min_i = j
    x_line[i], x_line[min_i] = x_line[min_i], x_line[i]

for i in range(len(y_line) - 1):
    min_i = i
    for j in range(i+1, len(y_line)):
        if y_line[min_i] > y_line[j]:
            min_i = j
    y_line[i], y_line[min_i] = y_line[min_i], y_line[i]

# 사각형들 중에 넓이가 가장 큰 값 찾기
max_a = max_b = 0
for i in range(1, len(x_line)):
    a = x_line[i] - x_line[i-1]
    if a > max_a:
        max_a = a
for i in range(1, len(y_line)):
    b = y_line[i] - y_line[i-1]
    if b > max_b:
        max_b = b
print(max_a * max_b)



