N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x:(x[1],x[0]))

cnt = 1
end = lst[0][1]
for i in range(1, N):
    if lst[i][0] >= end:
        cnt += 1
        end = lst[i][1]
print(cnt)