N, K = map(int, input().split())

visited = [0] * 100001
queue = [N]

while queue:
    q = queue.pop(0)

    if q == K:
        print(visited[q])
        break

    for i in (q-1, q+1, q*2):
        if 0 <= i < 100001 and not visited[i]:
            visited[i] = visited[q] + 1
            queue.append(i)


