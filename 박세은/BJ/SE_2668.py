def dfs(a):
    if a in first:
        return
    first.add(a)
    second.add(arr2[a-1])
    if first == second:
        for i in list(first):
            answer.add(i)
        return
    else:
        dfs(arr2[a-1])


N = int(input())
arr = list(i for i in range(1, N + 1))
arr2 = []
for i in range(N):
    arr2.append(int(input()))

answer = set()
for i in arr:
    if i not in answer:
        first = set()
        second = set()
        dfs(i)

answer = sorted(list(answer))
print(len(answer))
for i in answer:
    print(i)