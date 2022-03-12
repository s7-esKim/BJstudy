def check(t):
    stack = []

    for i in range(len(t)):
        if t[i] == '[' or t[i] == '(':
            stack.append(t[i])
        elif t[i] == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 'no'
            else:
                return 'no'
        elif t[i] == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
            else:
                return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'
while True:
    T = input()
    if T == '.':
        break
    print(check(T))