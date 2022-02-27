'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
# 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자
talk = ''
for i in range(5):
    talk = talk + ' ' + input()

talk = list(map(int, talk.split()))

talk_n = 0; 
def bingo_check(arr):
    bingo = 0
    diag_sum = 0
    reverse_diag_sum = 0
    for i in range(len(arr)):
        col_sum = 0
        diag_sum += arr[i][i]
        reverse_diag_sum += arr[i][len(arr)-i-1]
        if sum(arr[i]) == 0:
            bingo += 1
        for j in range(len(arr)):
            col_sum += arr[j][i]
        if col_sum == 0:
            bingo += 1
    if diag_sum == 0:
        bingo += 1
    if reverse_diag_sum == 0:
        bingo += 1
    return bingo
bingo_cnt = 0
while bingo_cnt < 3:

    for lst in bingo:
        for j in range(len(bingo)):
            if lst[j] == talk[talk_n]:
                lst[j] = 0
    if talk_n >=11:
        bingo_cnt = bingo_check(bingo)
    talk_n += 1

print(talk_n)
