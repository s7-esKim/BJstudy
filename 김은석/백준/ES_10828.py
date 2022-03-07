import sys

N = int(sys.stdin.readline())
stack = []

for tc in range(N):
    func = sys.stdin.readline().split()
    temp = func[0]

    if temp == 'push':
        stack.append(func[1])

    elif temp == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif temp == 'size':
        print(len(stack))

    elif temp == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif temp == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])