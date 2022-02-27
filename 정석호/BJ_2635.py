first_num = int(input())
num_len = 0
result = []

for i in range(first_num+1):
    gap_lst = [first_num, i]
    j = 0
    while True:
        num_gap = gap_lst[j] - gap_lst[j+1]
        j += 1
        if num_gap < 0:
            break
        gap_lst.append(num_gap)

        if num_len < len(gap_lst):
            num_len = len(gap_lst)
            result = gap_lst

print(num_len)
print(*result)



