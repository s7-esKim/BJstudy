N = int(input())
# 파이썬 튜플 정렬 이용 
# y축 좌표먼저 받고 정렬시키면 y , x 순으로 정렬
lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append((y, x))

lst.sort()

for x, y in lst:
    print(y, x)