import sys

open_b = ['[','(']
close_b = [']', ')']
while True:
    sentence = sys.stdin.readline().rstrip()
    stack = []
    if sentence == '.':
        break
    check = 1
    for i in sentence:
        if i == '.':
            break
        if i in open_b:
            stack.append(i)
        elif i in close_b:
            if stack:
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    check = 0
                    break
            else:
                check = 0
                break
    if not stack and check:
        print('yes')
    else:
        print('no')
