N, M = map(int, input().split())
if N > M: N, M = M, N
num1 = N 
num2 = M 
a = 0

while True:
    if not M % N:
        a = N
        break
    else:
        M, N = N, M % N

b = num1 * num2 / a

print(a, int(b))