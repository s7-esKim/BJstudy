import sys
input = sys.stdin.readline


S = int(input()) # 크기

lst = list(map(int,input().split()))
sum_lst = [0]*(sum(lst)+2)
sum_lst[0] = 1

for i in range(1 << S):
    sub_lst = []
    for j in range(S):
        if i & (1 << j):
            sub_lst.append(lst[j])

    sum_lst[sum(sub_lst)] = 1

print(sum_lst.index(0))