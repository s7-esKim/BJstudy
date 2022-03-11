import sys

a = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    arr = sys.stdin.readline().split()
    if arr[0] == 'L' and len(a) != 0:
        stack.append(a.pop())
    elif arr[0] == 'D' and len(stack) != 0:
        a.append(stack.pop())
    elif arr[0] == 'B' and len(a) != 0:
        a.pop()
    elif arr[0] == 'P':
        a.append(arr[1])

print(''.join(a + stack[::-1]))