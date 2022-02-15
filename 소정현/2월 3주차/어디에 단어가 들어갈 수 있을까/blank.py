import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def row_check(arr, K):
    # print(arr)
    tot = 0
    for lst in arr:
        word_n = 0
        for i in range(len(lst)):
            if lst[i] == 0:
                if word_n == K:
                    tot += 1
                word_n = 0
            else:
                word_n += 1
                if i == len(lst)-1 and word_n == K:
                    tot += 1
    return tot


def make_col_lst(arr):
    col_arr = []
    for i in range(len(arr)):
        col_lst = []
        for j in range(len(arr)):
            col_lst.append(arr[j][i])
        col_arr.append(col_lst)
    return col_arr

for ts in range(T):
    N, K = map(int, input().split())
    blank_arr = [list(map(int, input().split())) for _ in range(N)]
    row_result = row_check(blank_arr, K)
    col_blank = make_col_lst(blank_arr)
    col_result = row_check(col_blank, K)
    # print(row_result, col_result)
    print(f'#{ts+1} {row_result + col_result}')