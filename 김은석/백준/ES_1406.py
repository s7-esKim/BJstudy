import sys

stack1 = list(input())
stack2 = []
n = int(input())

for i in range(n):
    text = sys.stdin.readline().split()

    if text[0] == "L" and stack1:
        stack2.append(stack1.pop())
    elif text[0] == "D" and stack2:
        stack1.append(stack2.pop())
    elif text[0] == "B" and stack1:
        stack1.pop()
    elif text[0] == "P":
        stack1.append(text[1])

print("".join(stack1 + list(reversed(stack2))))