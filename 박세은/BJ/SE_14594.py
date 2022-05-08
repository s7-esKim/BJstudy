N = int(input())
T = int(input())

arr = [0] * (N+1)
for i in range(T):
    a, b = map(int, input().split())
    for j in range(a, b):
        arr[j] = 1

answer = arr.count(0)
print(answer - 1)