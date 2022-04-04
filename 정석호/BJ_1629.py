A, B, C = map(int, input().split())

def cal(a, b):
    if b == 1:
        return a % C
    else:
        if b % 2 == 0:
            temp = cal(a, b//2)
            return temp * temp % C
        else:
            temp = cal(a, b//2)
            return temp * temp * a % C

print(cal(A, B))

