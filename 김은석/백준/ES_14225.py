# 시간초과 코드
# S = int(input())
# lst = list(map(int, input().split()))
# ans = []
# for i in range(1<<len(lst)):
#     mysum = 0
#     for j in range(len(lst)):
#         if i & (1<<j):
#             mysum += lst[j]
#     ans.append(mysum)
# ans.sort()
# ans = ans[1:]
#
# min_value = 1
#
# while True:
#     if min_value not in ans:
#         break
#     min_value += 1
#
# print(min_value)

def DFS(n, k):
    visited[k] = 1
    if n == S:
        return
    else:
        DFS(n+1, k)
        DFS(n+1, k+lst[n])

S = int(input())
lst = list(map(int, input().split()))
visited = [0] * (sum(lst)+2)
DFS(0,0)
# print(visited)
print(visited.index(0))
