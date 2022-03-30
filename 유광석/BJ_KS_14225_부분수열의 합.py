# 메모리 64656kb, 시간 4680ms - python 3
# N = int(input())
# num_list = list(map(int,input().split()))

# sum_lst = set()

# for i in range(1, 1 << N):
#     tmp = []
#     for j in range(N):
#         if i & (1<<j):
#             tmp.append(num_list[j])
    
#     sum_lst.add(sum(tmp))

# for i in range(1, 100000*20):
#     if i not in sum_lst:
#         print(i)
#         break



# 메모리 103212kb, 시간 724ms - python 3
from itertools import combinations
N = int(input())
num_list = list(map(int,input().split()))

sum_lst = set()

for i in range(1, N+1):
    ssum = list(combinations(num_list, i))
    print(ssum)
    for j in ssum:
        sum_lst.add(sum(j))

for i in range(1, 100000*20):
    if i not in sum_lst:
        print(i)
        break



# 메모리 64656kb, 시간 1060ms - python 03
def nCr(n, r, s):
    if r == 0:
        sum_lst.add(sum(comb))
    else:
        for i in range(s, n-r+1):
            comb[r-1] = num_list[i]
            nCr(n, r-1, i+1)

N = int(input())
num_list = list(map(int,input().split()))
sum_lst = set()

for i in range(1, N+1):
    comb = [0] * i
    nCr(N, i, 0)

for i in range(1, 100000*20):
    if i not in sum_lst:
        print(i)
        break

    