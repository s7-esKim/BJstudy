import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def make_dict(lst):
    sdoku_dict = {}
    for i in lst:
        if i in sdoku_dict.keys():
            sdoku_dict[i] += 1
        else:
            sdoku_dict[i] = 1
    return sdoku_dict

def row_check(arr):
    for lst in arr:
        sdoku_dict = make_dict(lst)
        # print(lst, sdoku_dict)
        for _, value in sdoku_dict.items():
            if value > 1:
                return 1
    else:
        return 0

def make_col_lst(arr):
    col_arr = []
    for i in range(len(arr)):
        col_lst = []
        for j in range(len(arr)):
            col_lst.append(arr[j][i])
        col_arr.append(col_lst)
    return col_arr

def col_check(arr):
    col_arr = arr
    col_arr = make_col_lst(col_arr)

    for lst in col_arr:
        sdoku_dict = make_dict(lst)
        for _, value in sdoku_dict.items():
            if value > 1:
                return 1
    else:
        return 0
def box_idx(i, j):
    return i+3, j+3


for ts in range(T):
    sdoku_arr = [list(map(int, input().split())) for _ in range(9)]
    tot = 0
    col_result = col_check(sdoku_arr); row_result = row_check(sdoku_arr)
    tot += col_result
    tot += row_result

    for i in range(len(sdoku_arr)):
        for j in range(len(sdoku_arr)):
            if i % 3 == 0 and j % 3 == 0 :
                box_i, box_j = box_idx(i, j)
                box_lst = []
                for b_i in range(i, box_i):
                    for b_j in range(j, box_j):
                        box_lst.append(sdoku_arr[b_i][b_j])
                box_dict = make_dict(box_lst)
        for _, values in box_dict.items():
            if values > 1:
                tot += 1
    if tot == 0:
        print(f'#{ts+1} 1')
    else:
        print(f'#{ts+1} 0')