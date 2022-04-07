A, B, C = map(int, input().split())

def f(A, B, C):
    if B == 1:
        return A%C
    else:
        n = f(A, B//2, C)
        if B % 2:
            return n*n*A%C
        else:
            return n*n%C

print(f(A,B,C))
    