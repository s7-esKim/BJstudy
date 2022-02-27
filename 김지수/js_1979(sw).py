import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K)
    # print(arr)
    total = 0
    #가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1:
                if cnt == K:
                    total += 1
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N - 1:
                if cnt == K:
                    total += 1
                cnt = 0
    print(f'#{tc} {total}')
# 버블정렬
# 오->왼

# for i in range(len(arr)):
#     for j in range(len(arr)-1, i, -1):
#         if arr[j] > arr[j-1] :
#             arr[j], arr[j-1] = arr[j-1], arr[j]
# 왼->오
# for i in range(len(arr)-1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)
# arr = [0,2,2,3,2,5,4,8,10]
# cnt = [0] * 11 #len(arr) = 9
# for i in range(9):
#     cnt[arr[i]] += 1
# print(cnt)
# result = []
# for i in range(len(cnt)):
#     for j in range(cnt[i]):
#         result.append(i)
# print(result)
# new = []
# for i1 in range(1,5):
#     for i2 in range(1,5):
#         if i1 != i2:
#             for i3 in range(1,5):
#                 if i3 != i2 and i3 != i1:
#                     for i4 in range(1,5):
#                         if i4 != i1 and i4 != i2 and i3 != i4:
#                             new.append(i1)
#                             new.append(i2)
#                             new.append(i3)
#                             new.append(i4)
# n = 4
# # result = [new[i * n:(i+1)*n] for i in range((len(new) + n - 1) // n)]
# # result = [new[i:i+n] for i in range(0, len(new), n)]
# result = []
# for i in range(0, len(new), n):
#     result.append(new[i:i+n])
# print(result)