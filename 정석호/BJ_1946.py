T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    lst.sort()
    end = lst[0][1]
    cnt = 1
    for i in range(1, N):
        if lst[i][1] < end:
            cnt += 1
            end = lst[i][1]
    print(cnt)
