import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def remain_money(money, remain):
    return money//remain, money % remain

for ts in range(T):
    money = int(input())
    remain_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    remain_n = []
    for i in remain_lst:
        n, money = remain_money(money, i)
        remain_n.append(n)

    print(f"#{ts+1}\n{' '.join(list(map(str,remain_n)))}")