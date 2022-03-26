E = int(input())

V = E + 1
ch1 = [0 for _ in range(V+1)]
ch2 = [0 for _ in range(V+1)]

for i in range(E):
    x, y, z = input().split()
    if y != '.':
        ch1[ord(x) - 64] = y
    if z != '.':
        ch2[ord(x) - 64] = z

def pre_order(s):
    if s:
        print(s, end='')
        pre_order(ch1[ord(s) - 64])
        pre_order(ch2[ord(s) - 64])

def in_order(s):
    
    if s:
        in_order(ch1[ord(s) - 64])
        print(s, end='')
        in_order(ch2[ord(s) - 64])

def post_order(s):
    if s:
        post_order(ch1[ord(s) - 64])
        post_order(ch2[ord(s) - 64])
        print(s, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')