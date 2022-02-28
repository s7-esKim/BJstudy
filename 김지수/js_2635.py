# 첫번째 = 양의정수 100
# 두번째 = 양의 정수 중 하나 선택 1~99
# 세번째 = 앞앞 - 앞
# 네번째 = 앞앞 - 앞 ......
# 최대로 이어지는 수를 구하는 프로그램 구현
#
# import sys
# sys.stdin = open('1.txt')
n = int(input())
mlst = []
for i in range(1, n+1):
    temp = [n, i]
    num = 1
    while True:
        next = temp[num - 1] - temp[num]
        if next < 0:
            break
        temp.append(next)
        num += 1
    if len(temp) > len(mlst):
        mlst = temp

print(len(mlst))
print(*mlst)
