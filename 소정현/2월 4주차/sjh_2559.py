temp, day = map(int, input().split())

temp_lst = list(map(int, input().split()))

def lst_sum(lst):
    tot = 0
    for i in lst:
        tot += i
    return tot

max_sum = lst_sum(temp_lst[0:day])
day_temp = max_sum
for i in range(1, temp-day+1):
    # print(f'{i}th',max_sum,temp_lst[i-1], temp_lst[i+day-1])
    day_temp = day_temp - temp_lst[i-1] + temp_lst[i+day-1]    
    # print(day_temp)
    if  day_temp > max_sum:
        max_sum = day_temp 

print(max_sum)