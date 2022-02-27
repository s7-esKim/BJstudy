N = int(input())
b_lst = []
for _ in range(N):
    build = list(map(int, input().split()))
    b_lst.append(build)
b_lst.sort()

max_len = 0
max_idx = 0
for i in range(N):
    if max_len < b_lst[i][1]:
        max_len = b_lst[i][1]
        max_idx = b_lst[i][0]

start = 0
area = 0
for k in range(N):
    if b_lst[start][1] < b_lst[k][1]:
        area += (b_lst[k][0] - b_lst[start][0]) * b_lst[start][1]
        start = k

b_lst.reverse()
end = 0
for j in range(N):
    if b_lst[end][1] < b_lst[j][1]:
        area += ((b_lst[end][0]) - b_lst[j][0]) * b_lst[end][1]
        end = j

b_lst.sort()
for l in range(N):
    if max_len == b_lst[l][1]:
        area += (b_lst[l][0] - max_idx) * max_len
        max_idx = b_lst[l][0]

area += max_len
print(area)

