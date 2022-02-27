N, K = map(int, input().split())
lst = list(map(int, input().split()))
sum_1 = sum(lst[:K])
result = [sum_1]
for i in range(0, len(lst)-K):
    sum_1 = sum_1 - lst[i] + lst[i+K]
    result.append(sum_1)
print(max(result))



