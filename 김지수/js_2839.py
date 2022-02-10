# 설탕배달
# 배달해야 하는 설탕 무게 = N (kg) 5000>= N >= 3
# 설탕 봉지의 종류 3kg or 5kg
# 3*x + 3*y = N 일때 x+y 구하기
# 3*x + 3*y != N 이면 -1반환
n = int(input()) # N = 18

total = 0

while n>=0:
    if n % 5 == 0:
        total += n//5
        print(total)
        break
    n -= 3
    total += 1
else:
    print(-1)
