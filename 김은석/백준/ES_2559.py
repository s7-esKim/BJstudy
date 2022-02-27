N, K = map(int, input().split())
temp = list(map(int, input().split()))

value = sum(temp[:K])
max_temp = value

for i in range(N-K):
    value = value - temp[i] + temp[i+K]
    max_temp = max(max_temp, value)

print(max_temp)
