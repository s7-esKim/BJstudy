from itertools import permutations

T = int(input())
for ts in range(T):
    N = int(input())
    chess = [i for i in range(1,N+1)]

    chess_lst = list(permutations(chess, len(chess)))

    cnt = 0
    for lst in chess_lst:
        lst = list(lst)
        check = 0
        for i in range(len(lst)-1):
            for j in range(i+1, len(lst)):
                if abs(lst[i] - lst[j]) == abs(i - j):
                    check = 1
                    break
            if check:
                break
        else:
            cnt += 1

    print(f'#{ts+1} {cnt})