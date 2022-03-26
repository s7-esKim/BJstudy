V = int(input())
tree = [[] for _ in range(V+1)]

for i in range(V):
    arr = list(map(int, input().split()))
    p = arr[0]
    for j in range(1, len(arr)-1, 2):
        tree[p].append([arr[j], arr[j+1]])
# print(tree)


def search(start, visited):
    for i in tree[start]:
        end = i[0]
        if visited[end] == 0:
            visited[end] = visited[start] + i[1]
            search(end, visited)


visited1 = [0] * (V+1)
search(1, visited1)
visited1[1] = 0
# print(visited1)

max_distance = 0
max_index = 0
for i in range(len(visited1)):
    if max_distance < visited1[i]:
        max_distance = visited1[i]
        max_index = i

visited2 = [0] * (V+1)
search(max_index, visited2)
visited2[max_index] = 0
print(max(visited2))