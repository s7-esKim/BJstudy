import sys

# char = list(input())
char = list(sys.stdin.readline().strip())
# N = int(input())
N = int(sys.stdin.readline())
cursor = len(char)
temp = []
for i in range(N):
    # c = input().split()
    c = sys.stdin.readline().strip().split()

    if c[0] == 'P':
        char.append(c[1])
    elif c[0] == 'L' and char:
        temp.append(char.pop())
    elif c[0] == 'D' and temp:
        char.append(temp.pop())
    elif c[0] == 'B' and char:
        char.pop()

char = char + temp[::-1]
for c in char:
    print(c,end='')         #시간초과2
    # print(''.join(char))      #시간초과1