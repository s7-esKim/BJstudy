n = int(input())

for i in range(n):
    tot_score = 0
    correct = input().upper().split('X')
    for j in correct:
        lst = [k for k in range(1, len(j)+1)]
        tot_score += sum(lst)
    print(tot_score)