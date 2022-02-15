import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def sum_lst(array_lst):
    tot = 0
    for lst in array_lst:
        for i in lst:
            tot += i
    return tot


def make_array(array_lst, i , j, M):
    array_fly = []
    for n in range(M):
        fly_lst = array_lst[i:i+M]
        # [[1,3,3,6,7][8,13,9,12,8]]
        array_fly.append(fly_lst[n][j:j+M])
        # [[1,3],[8,13]]
    # print(array_fly)
    return array_fly


def kill_fly(lst, N, M):
    max_kill = 0
    if N==M:
        max_kill = sum_lst(lst)
    else:
        for i in range(N-M+1):
            for j in range(N-M+1):
                array = make_array(lst, i, j, M)
                if sum_lst(array) >= max_kill:
                    max_kill = sum_lst(array)

    return max_kill



for i in range(T):
    N, M = map(int, input().split())
    fly_lst = []
    for j in range(N):
        fly_lst.append(list(map(int, input().split())))
    max_kill = kill_fly(fly_lst, N, M)
    print(f'#{i+1} {max_kill}')