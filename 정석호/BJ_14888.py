def dfs(total, idx, plus, minus, mul, div):
    global max_num, min_num

    if idx == N:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return

    if plus:
        dfs(total+num[idx], idx+1, plus-1, minus, mul, div)
    if minus:
        dfs(total-num[idx], idx+1, plus, minus-1, mul, div)
    if mul:
        dfs(total*num[idx], idx+1, plus, minus, mul-1, div)
    if div:
        dfs(int(total/num[idx]), idx+1, plus, minus, mul, div-1)

N = int(input())
num = list(map(int, input().split()))
lst = list(map(int, input().split()))

max_num = -10**8
min_num = 10**8

dfs(num[0], 1, lst[0], lst[1], lst[2], lst[3])

print(max_num)
print(min_num)