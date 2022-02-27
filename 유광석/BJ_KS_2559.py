# 맞춘 코드 (증가할때마다 앞 뒤 값을 빼주면서 계산해줌)
totaldays, days = map(int, input().split())
temp_list = list(map(int, input().split()))
max_v = sum(temp_list[0:days])
num = sum(temp_list[0:days])

for i in range(totaldays - days):
    num = num - temp_list[i] + temp_list[i+days]
    if num > max_v:
        max_v = num
print(max_v)


# 시간초과 코드 (전부 비교하면서 돌면 시간초과!)
totaldays, days = map(int, input().split())
temp_list = list(map(int, input().split()))
max_v = []
for i in range(totaldays - days):
    max_v.append(sum(temp_list[i:i+days]))
print(max(max_v))