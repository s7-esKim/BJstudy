N = int(input())
time_lst = []
for _ in range(N):
    s, e = map(int, input().split())
    time_lst.append((s, e))

time_lst.sort(key= lambda x : (x[-1], x[0]))

cnt = 1
e = time_lst[0][1]
for i in range(1, N):
    if time_lst[i][0] >= e:
        e = time_lst[i][1]
        cnt += 1
print(time_lst)
print(cnt)

