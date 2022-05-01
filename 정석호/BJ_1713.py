N = int(input())
M = int(input())
rec = list(map(int, input().split()))

result = []
num = []

for i in range(M):
    if rec[i] in result:
        for j in range(len(result)):
            if rec[i] == result[j]:
                num[j] += 1
    else:
        if len(result) >= N:
            for j in range(N):
                if num[j] == min(num):
                    del result[j]
                    del num[j]
                    break
        result.append(rec[i])
        num.append(1)

result.sort()
print(*result)