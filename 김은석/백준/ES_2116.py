def check(li, num):
  for i in range(0,6):
    if num == li[i]:
      idx = i
      break
  if idx == 0:
    return (max(li[1], li[2], li[3], li[4]) , li[5])
  elif idx == 5:
    return (max(li[1], li[2], li[3], li[4]) , li[0])
  elif idx == 1:
    return (max(li[0], li[2], li[5], li[4]) , li[3])
  elif idx == 3:
    return (max(li[0], li[2], li[5], li[4]) , li[1])
  elif idx == 2:
    return (max(li[0], li[1], li[5], li[3]), li[4])
  elif idx == 4:
    return (max(li[0], li[1], li[5], li[3]), li[2])


N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
max_side = 0

for i in range(1,7):
    a = i
    temp = 0
    for j in range(N):
        sum_dice, a = check(dice[j],a)
        temp += sum_dice
    if max_side < temp:
        max_side = temp

print(max_side)

