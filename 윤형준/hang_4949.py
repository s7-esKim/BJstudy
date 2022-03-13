while True:
    stc = input()
    stack = []
    if stc == '.':
        break
    flag = 1
    for i in stc:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                flag = 0
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                flag = 0
                break
    if flag == 0:
        continue
    if not stack:
        print('yes')
    else:
        print('no')