def list_sort(li):
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li

x, y  = map(int, input().split())
garo = [0, y]
sero = [0, x]
T = int(input())
for ts in range(T):
    d, l = map(int, input().split())
    if d:
        sero.append(l)
    else:
        garo.append(l)

max_x = 0
max_y = 0
s_garo = list_sort(garo)
s_sero = list_sort(sero)

for i in range(len(s_garo) - 1):
    if s_garo[i + 1] - s_garo[i] > max_x:
        max_x = s_garo[i + 1] - s_garo[i]

for j in range(len(s_sero) - 1):
    if s_sero[j + 1] - s_sero[j] > max_y:
        max_y = s_sero[j + 1] - s_sero[j]

print(max_x * max_y)




    