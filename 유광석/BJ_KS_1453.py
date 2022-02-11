#피시방 알바
# 1~100 컴퓨터, 원하는 자리에 앉고 자리가 있으면 거절

N = int(input())
custumers = list(map(int, input().split()))
arr = [0 for i in range(100)]
ans = 0

for i in custumers:
    arr[i-1] += 1
    if arr[i-1] >= 2:
        ans += 1

print(ans)