import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def check_up(num):
    num = str(num)
    if len(num) == 1:
        return int(num)
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if int(num[i]) > int(num[j]):
                return -1
    return int(num)


for ts in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    max_k = -1
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            result = lst[i] * lst[j]
            result = check_up(result)
            if result > max_k:
                max_k = result
    print(f'#{ts+1} {max_k}')