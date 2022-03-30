# N = int(input())
# visited = []
# cnt = 0

# def check(y):
#     global cnt

#     if y == N:
#         cnt += 1
#         return
    
#     for i in range(N):
#         if i not in visited:
#             for j in range(y):
#                 if abs(visited[j] - i) == y - j:
#                     break
#             else:
#                 visited.append(i)
#                 check(y+1)
#                 visited.pop()

# check(0)
# print(cnt)

def check(r):
    global cnt

    if r == N:
        cnt += 1
        return

    for i in range(N):
        if i not in visited:
            for j in range(r):
                if visited[j] - i == r - j or i - visited[j] == r - j:
                    break
            else:
                visited.append(i)
                check(r+1)
                visited.pop()

N = int(input())
cnt = 0
visited = []
check(0)
print(cnt)