N = int(input())
rect = [list(map(int, input().split())) for _ in range(N)]
rect.sort()

height = 0
left = 0
answer = 0
for i in rect:
    if height <= i[1]:
        answer += (i[0] - left)*height
        height = i[1]
        left = i[0]

height = 0
left = 0
rect.reverse()
for j in rect:
    if height <= j[1]:
        answer += (left - j[0])*height
        height = j[1]
        left = j[0]

left = 0
h_t = 0
for k in rect:
    if height == k[1]:
        answer -= (left - k[0])*h_t
        left = k[0]
        h_t = k[1]
answer += height
print(answer)



