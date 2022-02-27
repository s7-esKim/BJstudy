n = int(input())
dice = [[] for _ in range(n)]
result = 0
for i in range(n):
    num = list(map(int, input().split()))
    dice[i].append((num[0], num[5]))
    dice[i].append((num[1], num[3]))
    dice[i].append((num[2], num[4]))

def sol():
    for d in dice[0]:
        for t in d:
            select_num(t)
    print(result)

def select_num(t):
    global result
    total = 0
    for i in range(n):
        for d in dice[i]:
            if t in d:
                if 6 in d:
                    if 5 in d:
                        total += 4
                    else:
                        total += 5
                else:
                    total += 6
                if t == d[0]:
                    t = d[1]
                    break
                else:
                    t = d[0]
                    break
    result = max(result, total)
sol()