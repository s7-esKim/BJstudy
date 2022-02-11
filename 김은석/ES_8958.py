T = int(input())

for tc in range(T):
    OX = input()
    cnt = 0
    cnt2 = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            cnt += 1
            cnt2 += cnt
        else:
            cnt = 0
    print(cnt2)


