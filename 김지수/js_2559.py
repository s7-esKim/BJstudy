import sys
sys.stdin = open('1.txt')
total, day = map(int, input().split())
lst = list(map(int, input().split()))
result = []
for i in range(total - day):
    temp = 0
    for j in range(day):
        temp += lst[j+i]
    result.append(temp)
print(max(result))
