# import sys
# sys.stdin = open('input.txt')


N = int(input())
arr_A = list(map(int, input().split()))
arr_B = arr_A[:]

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr_B[j] > arr_B[j+1]:
            arr_B[j], arr_B[j+1] = arr_B[j+1], arr_B[j]

answer = []
for i in range(N):
    for j in range(N):
        if arr_A[i] == arr_B[j]:
            answer.append(j)
            arr_B[j] = 0
            break
print(*answer)
