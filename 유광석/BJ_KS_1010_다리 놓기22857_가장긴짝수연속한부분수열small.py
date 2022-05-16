# import sys
# sys.setrecursionlimit(10**6)

# def check(idx, k, cnt):
#     global ans
    
#     if cnt > ans:
#         ans = cnt

#     if idx >= N:
#         return


#     if arr[idx] % 2 == 0:
#         cnt += 1
#         check(idx+1, k, cnt)
#     else:
#         check(idx+1, k, 0)
#         if k > 0:
#             k -= 1
#             check(idx+1, k, cnt)

# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# ans = 0
# check(0, K, 0)
# print(ans)

N, K = map(int, input().split())
arr = list(map(int, input().split()))
d = [[0 for _ in range(K+1)] for _ in range(N)]

if arr[0] % 2 == 0:
    for j in range(K+1):
        d[0][j] = 1

for i in range(1, N):
    if arr[i] % 2 == 0:
        for j in range(K+1):
            d[i][j] = d[i-1][j] + 1
    else:
        for j in range(1, K+1):
            d[i][j] = d[i-1][j-1]

print(max(map(max, d)))