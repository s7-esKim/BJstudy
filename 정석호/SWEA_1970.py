T = int(input())
for tc in range(1, T+1):
    money = int(input())
    exchange = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_cnt = [0] * 8

    while money >= 0:
        for i in range(len(exchange)):
            if money // exchange[i] > 0:
                money_cnt[i] += money // exchange[i]
                money = money % exchange[i]
        else:
            break
    print(f'#{tc}')
    print(*money_cnt)


