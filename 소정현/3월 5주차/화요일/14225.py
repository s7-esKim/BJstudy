import sys
input = sys.stdin.readline


def make_dict(s):
    sum_dict = {}
    for i in range(1,s+2):
        sum_dict[i] = 0
    return sum_dict

S = int(input()) # 크기

lst = list(map(int,input().split()))
sum_dict = make_dict(sum(lst))

for i in range(1 << S):
    sub_lst = []
    for j in range(S):
        if i & (1 << j):
            sub_lst.append(lst[j])

    sum_dict[sum(sub_lst)] = 1


for key, value in sum_dict.items():
    if value == 0:
        print(key)
        break