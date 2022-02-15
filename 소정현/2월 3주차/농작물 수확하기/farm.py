import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def arr_sum(arr):
    tot = 0
    for lst in arr:
        lst_sum = 0
        for i in lst:
            lst_sum += i
        tot += lst_sum
    return tot

for ts in range(T):
    N = int(input())
    farm_lst = [list(map(int, input())) for _ in range(N)]
    farm_center = int((N-1)/2)
    choice_farm = []
    max_i = farm_center; min_i = farm_center
    for i in range(N):
        if 0 < i <= farm_center:
            max_i += 1
            min_i -= 1
            choice_farm.append(farm_lst[i][min_i : max_i+1])
        elif farm_center < i < N-1:
            max_i -= 1
            min_i += 1
            choice_farm.append(farm_lst[i][min_i: max_i + 1])
        else:
            choice_farm.append([farm_lst[i][farm_center]])

    print(f'#{ts+1} {arr_sum(choice_farm)}')