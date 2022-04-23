N = int(input())

result = cnt = 0
while cnt < N:
    result += 1
    if cnt + 3 <= N:
        cnt += 3
    else:
        cnt += 1

if result % 2:
    print('SK')
else:
    print('CY')