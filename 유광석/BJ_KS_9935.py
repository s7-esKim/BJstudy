import sys
T = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

stack = []

for i in range(len(T)):
    stack.append(T[i])
    if len(stack) >= len(t):
        if stack[-len(t):] == t:        # 음수 슬라이싱!!!!!!
            for i in range(len(t)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')



