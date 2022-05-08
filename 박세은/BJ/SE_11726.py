arr = [0] * 1001
arr[1] = 1
arr[2] = 2

for i in range(3, 1001):
    arr[i] = sum(arr[i-2:i])

N = int(input())
print(arr[N] % 10007)