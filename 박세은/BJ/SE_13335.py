# N : 트럭수, W : 다리길이, L : 최대하중
N, W, L = map(int, input().split())
arr = list(map(int, input().split()))

stack = [0] * W
answer = 0
while stack:
    answer += 1
    stack.pop(0)
    if arr:
        if sum(stack) + arr[0] <= L:
            stack.append(arr.pop(0))
        else:
            stack.append(0)
print(answer)
