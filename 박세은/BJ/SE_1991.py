def preorder(alphabet):
    for i in range(len(p)):
        if alphabet == p[i]:
            v = i
            print(p[v], end='')
            preorder(ch1[v])
            preorder(ch2[v])


def inorder(alphabet):
    for i in range(len(p)):
        if alphabet == p[i]:
            v = i
            inorder(ch1[v])
            print(p[v], end='')
            inorder(ch2[v])


def postorder(alphabet):
    for i in range(len(p)):
        if alphabet == p[i]:
            v = i
            postorder(ch1[v])
            postorder(ch2[v])
            print(p[v], end='')


N = int(input())
p = [0] * N
ch1 = [0] * N
ch2 = [0] * N

for i in range(N):
    P, C1, C2 = map(str, input().split())
    p[i] = P
    if C1 != '.' and ch1[i] == 0:
        ch1[i] = C1
    if C2 != '.':
        ch2[i] = C2

preorder('A')
print()
inorder('A')
print()
postorder('A')