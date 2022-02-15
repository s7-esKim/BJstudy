import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def change_num(str):
    if str == 'ZRO':
        return 0
    elif str == 'ONE':
        return 1
    elif str == 'TWO':
        return 2
    elif str == 'THR':
        return 3
    elif str == 'FOR':
        return 4
    elif str =='FIV':
        return 5
    elif str == 'SIX':
        return 6
    elif str == 'SVN':
        return 7
    elif str == 'EGT':
        return 8
    else:
        return 9

def change_gns_num(lst):
    change_gns = []
    for i in lst:
        change_gns.append(change_num(i))
    return change_gns


for i in range(T):
    num, case_n= input().split()
    gns_lst = input().split()
    change_gns_lst = change_gns_num(gns_lst)
    for i in range(len(gns_lst)-1):
        for j in range(i+1, len(gns_lst)):
            if change_gns_lst[i] > change_gns_lst[j]:
                change_gns_lst[i], change_gns_lst[j] = change_gns_lst[j], change_gns_lst[i]
                gns_lst[i], gns_lst[j] = gns_lst[j], gns_lst[i]
    print(f"{num} {' '.join(gns_lst)}")