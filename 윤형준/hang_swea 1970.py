import sys
sys.stdin = open('input 1970.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    Money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt_lst = [0]*8

    for i in range(8):
        if N // Money[i]:
            cnt_lst[i] += N // Money[i]
            N = N % Money[i]


    print(f'#{tc}')
    print(*cnt_lst)