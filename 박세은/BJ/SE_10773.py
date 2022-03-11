N = int(input())  # 정수의 개수
arr = [int(input()) for _ in range(N)]
stack = []

for i in range(N):
    if arr[i] == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack.append(arr[i])

print(sum(stack))
