# OX퀴즈
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    ox_lst = list(input()) # O O X X O X X O O O

    cnt = 0
    total = 0 # 1
    for i in range(len(ox_lst)): # 0 1 2 3 4 5 6 7 8 9
        if ox_lst[i] == 'O':
            cnt += 1
            total += 1 * cnt
        else:
            cnt = 0
    print(total)
