import sys
input = sys.stdin.readline

N, S = map(int, input().split())

lst = list(map(int, input().split()))
cnt = 0
for i in range(1 << N):
    sub_lst = []
    for j in range(N):
        if i & (1 << j):
            sub_lst.append(lst[j])
    if sub_lst:
        if sum(sub_lst) == S:
            cnt += 1


print(cnt)