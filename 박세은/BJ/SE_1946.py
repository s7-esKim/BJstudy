import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())

    arr = []
    for i in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr = sorted(arr)

    count = 1
    interview = arr[0][1]
    for j in range(1, N):
        if arr[j][1] < interview:
            count += 1
            interview = arr[j][1]
    print(count)
