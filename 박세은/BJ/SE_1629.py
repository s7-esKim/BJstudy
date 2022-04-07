# 지수 법칙
# 짝수 : A**B = A**(B//2+B//2) = A**(B//2) * A**(B//2)
# 홀수 : A**B = A**(B//2+B//2+1) = A**(B//2) * A**(B//2) * A
# 나머지 분배 법칙 : (A*B) % C = ((A%C) * (B%C)) % C
def f(a, b):
    if b == 1:
        return a % C
    else:
        num = f(a, b//2)
        if b % 2 == 0:
            return num * num % C
        else:
            return num * num * a % C


A, B, C = map(int, input().split())
print(f(A, B))