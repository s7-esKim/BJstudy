V = int(input())
lst = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(V)]
visited = [0 for i in range(V)]
root = []

# 루트는 한개가 아닐 수도 있다...
for i in range(V):
    if lst[i] == -1:
        root.append(i)
    elif i == del_node:
        pass
    else:
        tree[lst[i]].append(i)


def find_leaf(s):
    leaf = 0
    stack = [s]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = +1
            if tree[v]:
                for i in tree[v]:
                    stack.append(i)
            else:
                leaf += 1
    return leaf

ans = 0
for i in root:
    if del_node == i:
        a = 0
    else:
        a = find_leaf(i)
    ans += a

print(ans)
