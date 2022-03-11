import sys

while True:
    arr = sys.stdin.readline().rstrip()
    if arr == '.':
        break
    stack = []
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0 and arr[-1] == '.':
        print('yes')
    else:
        print('no')