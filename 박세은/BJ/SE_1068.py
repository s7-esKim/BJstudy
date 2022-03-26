def dfs(num):
    global answer
    if not ch[num]:
        answer += 1
    else:
        for i in ch[num]:
            if i == D:
                if len(ch[num]) == 1:
                    answer += 1
            else:
                dfs(i)


N = int(input())
arr = list(map(int, input().split()))
D = int(input())
root = 0

ch = [[] for _ in range(N)]
for i in range(len(arr)):
    if arr[i] == -1:
        root = i
    else:
        ch[arr[i]].append(i)

answer = 0
if D == root:
    print(0)
else:
    dfs(root)
    print(answer)