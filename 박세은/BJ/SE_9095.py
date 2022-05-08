arr = [0] * 12
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 12):
    arr[i] = sum(arr[i-3:i])

T = int(input())
for tc in range(T):
    N = int(input())
    print(arr[N])
