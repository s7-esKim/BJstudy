N = int(input())

area = [list(map(int, input().split())) for _ in range(6)]
x = y = 0    # 가장 긴 가로, 세로
xi = yi = 0  # 가장 긴 가로, 세로의 index
x2 = y2 = 0

for i in range(6):
    if area[i][0] == 1 or area[i][0] == 2:
        if area[i][1] > x:
            x = area[i][1]
            xi = i
    if area[i][0] == 3 or area[i][0] == 4:
        if area[i][1] > y:
            y = area[i][1]
            yi = i

# 가장 긴 가로(세로)와 이어진 값들 중 큰 값 - 작은 값 = 작은 사각형의 가로(세로)
# index error : 더해줄 때는 6으로 나눈 나머지 활용
x2 = abs(area[yi-1][1] - area[(yi+1) % 6][1])
y2 = abs(area[xi-1][1] - area[(xi+1) % 6][1])

print((x*y - x2*y2) * N)  # (가장 큰 네모 - 작은 네모) * 참외 수
