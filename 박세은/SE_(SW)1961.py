import sys
sys.stdin = open('input.txt')


def turn_num(arr):
    N = len(arr)
    new_arr = []
    for i in range(N):
        a = ''
        for j in range(N-1, -1, -1):
            a += str(arr[j][i])
        new_arr.append(a)
    return new_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    turn1 = turn_num(arr)
    turn2 = turn_num(turn1)
    turn3 = turn_num(turn2)
    answer_list = [turn1, turn2, turn3]

    answer = ''
    for j in range(N):
        for i in answer_list:
            answer += i[j]
            answer += ' '
        if j == N-1:
            break
        answer += '\n'

    print(f'#{tc}\n{answer}')