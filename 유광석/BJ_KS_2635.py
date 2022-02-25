N = int(input())
result = 0
result_list = []
for x in range(1, N + 1):
    cnt = 1
    n_list = []
    s = N
    while True:
        n_list.append(s)
        a  = s - x
        s, x = x, a
        if s < 0:
            s = N
            break
        else:
            cnt += 1
    if cnt > result:
        result = cnt
        result_list = n_list

print(result)
print(*result_list)
    

