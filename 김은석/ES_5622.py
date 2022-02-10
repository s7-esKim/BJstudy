arr = list(input())
cnt = 0
for i in arr:
    if i == 'A' or i == 'B' or i == 'C':
       cnt += 3
    elif i == 'D' or i == 'E' or i == 'F':
        cnt += 4
    elif i == 'G' or i == 'H' or i == 'I':
        cnt += 5
    elif i == 'J' or i == 'K' or i == 'L':
        cnt += 6
    elif i == 'M' or i == 'N' or i == 'O':
        cnt += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        cnt += 8
    elif i == 'T' or i == 'U' or i == 'V':
        cnt += 9
    else:
        cnt += 10
print(cnt)