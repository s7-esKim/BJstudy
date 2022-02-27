n = int(input())

def make_lst(main_num, second_num):
    number_lst = [main_num, second_num]
    i = 0
    while True:
        if number_lst[i] - number_lst[i+1] >= 0:
            number_lst.append(number_lst[i]-number_lst[i+1])
        else:
            break
        
        i += 1
    return number_lst

def len_lst(lst):
    cnt = 0
    for i in lst:
        cnt += 1
    return cnt

best_lst = ''
best_cnt = 0

for i in range(1, n+1):
    lst = make_lst(n, i)
    if len_lst(lst) >= best_cnt:
        best_cnt = len_lst(lst)
        best_lst = ' '.join(list(map(str, lst)))

print(best_cnt)
print(best_lst)