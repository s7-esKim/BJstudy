sum_lst = [0] * 11
sum_lst[1] = 1
sum_lst[2] = 2
sum_lst[3] = 4
for i in range(4, 11):
    sum_lst[i] = sum_lst[i-3] + sum_lst[i-2] + sum_lst[i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(sum_lst[N])

