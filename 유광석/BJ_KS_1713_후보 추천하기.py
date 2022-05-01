N = int(input())
reco = int(input())
order = list(map(int, input().split()))

name = []
cnt = []

for i in range(reco):
    if order[i] in name:
        cnt[name.index(order[i])] += 1

    elif not name or len(name) < N:
        name.append(order[i])
        cnt.append(1)

    else:
        min_reco = 1000000
        min_i = 0
        for idx in range(N):
            if cnt[idx] < min_reco:
                min_reco = cnt[idx]
                min_i = idx
        
        a = name.pop(min_i)
        b = cnt.pop(min_i)
        name.append(order[i])
        cnt.append(1)

# ans = list(zip(name, cnt))
# ans.sort(key=lambda x:x[1], reverse=True)
name.sort()
for i in name:
    print(i, end=' ')

