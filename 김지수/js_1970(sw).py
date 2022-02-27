import sys
sys.stdin = open('input (1).txt')

T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    money_size = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    cnt = [0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        if money >= money_size[0]:
            cnt[0] += money // money_size[0]
            money = money % money_size[0]
        elif money >= money_size[1]:
            cnt[1] += money // money_size[1]
            money = money % money_size[1]
        elif money >= money_size[2]:
            cnt[2] += money // money_size[2]
            money = money % money_size[2]
        elif money >= money_size[3]:
            cnt[3] += money // money_size[3]
            money = money % money_size[3]
        elif money >= money_size[4]:
            cnt[4] += money // money_size[4]
            money = money % money_size[4]
        elif money >= money_size[5]:
            cnt[5] += money // money_size[5]
            money = money % money_size[5]
        elif money >= money_size[6]:
            cnt[6] += money // money_size[6]
            money = money % money_size[6]
        elif money >= money_size[7]:
            cnt[7] += money // money_size[7]
            money = money % money_size[7]
        else:
            break
    result = ' '.join(map(str, cnt))
    print(f'#{tc}\n{result}')