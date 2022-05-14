n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
start, end = 0, 0
size, size_max = 0, 0
flag = 1

for start in range(n):
    while cnt <= k and flag:
        if lst[end] % 2:
            if cnt == k:
                break
            cnt += 1
        size += 1
        if end == n - 1:
            flag = 0
            break
        end += 1

    if size_max < size - cnt:
        size_max = size - cnt

    if lst[start] % 2:
        cnt -= 1

    size -= 1

print(size_max)