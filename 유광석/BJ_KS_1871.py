T = int(input())

for ts in range(T):
    a, n = input().split('-')
    a_n = 0
    for i in range(len(a) - 1, -1, -1):
        a_n += (ord(a[i]) - 65) * 26 ** (len(a) - 1 - i)

    if abs(a_n - int(n)) <= 100:
        print('nice')
    else:
        print('not nice')
