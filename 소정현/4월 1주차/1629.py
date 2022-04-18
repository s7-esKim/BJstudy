import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
# A ^ B % C  = (A ^ (B//2) % C) * (A ^ (B//2) % C) * (A% C) % C

def multi(a, b):
    if b == 1:
        return a % c
    else:
        tmp = multi(a, b // 2)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(multi(a, b))
