import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def turn_degree(arr):
    turn_arr = []
    for i in range(len(arr)):
        turn_lst = []
        for j in range(len(arr)-1, -1, -1):
            turn_lst.append(arr[j][i])
        turn_arr.append(turn_lst)

    return turn_arr

def empty_turn(N):
    empty_arr = []
    for i in range(N):
        empty_arr.append([])
    return empty_arr

for ts in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    empty_arr = empty_turn(N)
    for i in range(3):
        arr = turn_degree(arr)
        for j in range(len(arr)):
            empty_arr[j].append(''.join(list(map(str, arr[j]))))
    print(f'#{ts+1}')
    for lst in empty_arr:
        print(' '.join(lst))
