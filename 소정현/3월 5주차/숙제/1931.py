import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

time_lst = [list(map(int, input().split())) for _ in range(N)]
time_lst.sort(key = lambda x : x[0]) # 먼저 시작하는 시간이 빠른 순
time_lst.sort(key = lambda x : x[1]) # 그 후로 끝나는시간이 겹치는 것중에 빠른 시간부터 시작하도록 설정
max_cnt = 0

def dfs(i, time, cnt):
    global max_cnt
    if i == N:
        max_cnt = max(max_cnt, cnt)
        return

    if time <= time_lst[i][0]:
        dfs(i+1, time_lst[i][1], cnt+1)
    else:
        dfs(i+1, time, cnt)

dfs(1, time_lst[0][1], 1)
print(max_cnt)