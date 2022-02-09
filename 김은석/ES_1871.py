N = int(input())

for i in range(N):
    alpha, num = input().split('-')
    real_num = int(num)

    ord_alpha = 0
    for j in range(3):
        ord_alpha += (ord(alpha[j]) - 65) * 26 ** (2 - j)

    if abs(ord_alpha - real_num) <= 100:
        print('nice')
    else:
        print('not nice')