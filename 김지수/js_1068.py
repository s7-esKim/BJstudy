def dfs(num, par):
    par[num] = -2
    for i in range(len(par)):
        if num == par[i]:
            dfs(i, par)

N = int(input())
par = list(map(int, input().split()))
d = int(input())

dfs(d, par)

cnt = 0
for i in range(len(par)):
    if par[i] != -2 and i not in par:
        cnt += 1
print(cnt)