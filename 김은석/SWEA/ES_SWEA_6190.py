def compare(number):
    a = 10
    b = number % 10
    while number:
        if a >= b:
            a = b
            number //= 10
            b = number % 10
        else:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))

    result = -1
    for i in range(N):
        for j in range(i+1, N):
            num = A[i] * A[j]
            if num > result and compare(num):
                result = num

    print(f'#{tc} {result}')





