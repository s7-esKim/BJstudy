import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def remove_lst(std_lst, check_lst):
    not_check = []
    for i in std_lst:
        if i not in check_lst:
            not_check.append(i)
    return not_check

for i in range(T):
    student, check = map(int, input().split())
    stud_lst = [i for i in range(1,student+1)]
    check_lst = list(map(int,input().split()))
    not_check = remove_lst(stud_lst, check_lst)
    result = ' '.join(list(map(str, not_check)))

    print(f'#{i+1} {result}')