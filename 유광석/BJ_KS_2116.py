def list_max(lis, num1, num2):
    max_v = 0
    for i in lis:
        if i == num1 or i == num2:
            continue
        else:
            if i >= max_v:
                max_v = i
    return max_v

def f_opp(li, num):
    for i in range(6):
        if li[i] == num:
            if i == 0:
                return li[5]
            elif i == 1:
                return li[3]
            elif i == 2:
                return li[4]
            elif i == 3:
                return li[1]
            elif i == 4:
                return li[2]
            else:
                return li[0]
                
N = int(input())
dice_list = []
ans = 0

for ts in range(N):
    another_dice = list(map(int, input().split()))
    dice_list.append(another_dice)

for i in range(1, 7):
    x_list = dice_list[:]
    x = 0
    for j in dice_list:
        bot = i
        top = f_opp(j, i)
        i = top
        x += list_max(j, bot, top)
    if ans <= x:
        ans = x

print(ans)
