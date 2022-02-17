N = int(input())
arr = list(map(int, input().split()))
temp = [0 for i in range(101)]
result = 0

for num in arr:
    if temp[num] != 0:
        result += 1
    else:
        temp[num] += 1

print(result)