from sys import stdin
input = stdin.readline

n = int(input())

dices = [[] for _ in range(n)]
answer = 0
for idx in range(n):
    nums = list(map(int, input().split()))

    dices[idx].append((nums[0],nums[5]))
    dices[idx].append((nums[1],nums[3]))
    dices[idx].append((nums[2],nums[4]))

def solv():
    for dice in dices[0]:
        for target in dice:
            select_num(target)
    print(answer)

def select_num(target):
    global answer
    total = 0
    for idx in range(n):
        for dice in dices[idx]:
            if target in dice:
                if 6 in dice:
                    if 5 in dice:
                        total += 4
                    else:
                        total += 5
                else:
                    total += 6
                if target == dice[0]:
                    target = dice[1]
                    break
                else:
                    target = dice[0]
                    break
    answer = max(answer,total)
solv()