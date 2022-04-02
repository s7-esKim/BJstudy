import sys
input = sys.stdin.readline

T = int(input())


def dp(i, lst):
    global max_cnt

    if i == N:
        max_cnt = max(max_cnt, len(lst))
        return
    if lst:
        for f, s in lst:
            if f > arr[i][0] and s > arr[i][1]:

for ts in range(T):
    N = int(input())
    arr = [map(int, input().split()) for _ in range(N)]
    max_cnt = 0