R, C = map(int, input().split())

chess = [list(input()) for _ in range(R)]


def make_dict(chess):
    chess_dict = {}
    for lst in chess:
        for i in lst:
            if i not in chess_dict.keys():


visit = [[0]*C for _ in range(R)]
visit[0][0] = 1
lst = []
max_cnt = 0

def dfs(i, j, cnt):
    global max_cnt
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    max_cnt = max(max_cnt, cnt)
    for k in range(4):
        if 0 <= i + di[k] < R and 0 <= j + dj[k] < C and chess[i+di[k]][j+dj[k]] not in lst:
            visit[i][j] = 1
            lst.append(chess[i+di[k]][j+dj[k]])
            dfs(i+di[k],j+dj[k],cnt+1)
            lst.pop()
            visit[i][j] = 0

print(max_cnt)


