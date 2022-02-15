T = int(input())

for tc in range(1, T+1):
    money = int(input())
    cnt =[0] * 8
    while money >= 10:
        if money >= 50000:
            cnt[0] += 1
            money -= 50000
        elif money >= 10000:
            cnt[1] += 1
            money -= 10000
        elif money >= 5000:
            cnt[2] += 1
            money -= 5000
        elif money >= 1000:
            cnt[3] += 1
            money -= 1000
        elif money >= 500:
            cnt[4] += 1
            money -= 500
        elif money >= 100:
            cnt[5] += 1
            money -= 100
        elif money >= 50:
            cnt[6] += 1
            money -= 50
        elif money >= 10:
            cnt[7] += 1
            money -= 10
        else:
            break
    print(f'#{tc}')
    print(*cnt)