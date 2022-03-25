def DFS(x):
    global ans
    if x not in lst and x != delete:
        ans += 1
        return
    else:
        for i in range(N):
            if lst[i] == x and i != delete:
                DFS(i)
    return ans

N = int(input())
lst = list(map(int, input().split()))
delete = int(input())

start = 0
for i in range(len(lst)):
    if lst[i] == -1:
        start = i

ans = 0

if start == delete:
    print(ans)

else:
    DFS(start)
    if lst.count(lst[delete]) == 1:
        ans += 1
    print(ans)
