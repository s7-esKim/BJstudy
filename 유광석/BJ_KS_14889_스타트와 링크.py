N = int(input())
arr= [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
min_v = 20*20*100
a = [i for i in range(1, N+1)]
set_a = set(a)

for i in range(1, 1 << N):
    tmp = []
    for j in range(N):
        if i & (1 << j):
            tmp.append(a[j])
    
    if len(tmp) == N//2:
        start = tmp
        link = list(set_a - set(tmp))
        ssum_start = 0
        ssum_link = 0

        for k in range(N//2):
            for l in range(k+1, N//2):
                ssum_start += arr[start[k]][start[l]] + arr[start[l]][start[k]]
                ssum_link += arr[link[k]][link[l]] + arr[link[l]][link[k]]
        ssum = abs(ssum_start - ssum_link)
        min_v = min(min_v, ssum)
    
print(min_v)