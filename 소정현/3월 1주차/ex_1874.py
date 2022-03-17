'''
8 
4 
3 
6 
8 
7 
5 
2 
1 
'''
T =int(input())

target_lst = [int(input()) for _ in range(T)]

lst = [];  my_lst = []
i = 1; idx = 0
pop_push_lst = []
target_true = 1
while my_lst != target_lst:
    if len(lst) == 0:
        lst.append(i)
        pop_push_lst.append('+')
        i += 1
    else:
        if lst[-1] > target_lst[idx]:
            print('NO')
            target_true = 0
            break

    if lst[-1] == target_lst[idx]:
        my_lst.append(lst.pop())
        pop_push_lst.append('-')
        idx += 1
    else:
        lst.append(i)
        pop_push_lst.append('+')
        i += 1

if target_true:
    print(*pop_push_lst, sep ='\n')
