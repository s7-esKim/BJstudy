import sys
sys.stdin = open('input.txt')


# 지금 가지고 있는 높이보다 더 큰값을 만나면
# 높이 * (지금 index - 그전의 index)
def store_area(s, e, num):
    b = 0
    x = 0
    ans = 0
    for i in range(s, e, num):
        if store[i] > b:
            ans += b * abs(i - x)
            b = store[i]
            x = i
    return ans


# N : 기둥의 개수
N = int(input())
list_s = []
for _ in range(N):
    stick = list(map(int, input().split()))
    list_s.append(stick)

# 기둥 높이 넣기
store = [0] * 1001
for i in range(N):
    store[list_s[i][0]] = list_s[i][1]

# 가장 높은 기둥의 index 값 찾기
max_list = []
for i in range(1001):
    if max(store) == store[i]:
        max_list.append(i)

# 처음 max 값까지 계속 올라가기
# max 구간 : (마지막 max - 처음 max + 1) * max 값
# 마지막부터 마지막 max 값으로 계속 올라가기
sum1 = store_area(0, max_list[0]+1, 1)
sum2 = store_area(1000, max_list[-1]-1, -1)
sum3 = max(store) * (max_list[-1] - max_list[0] + 1)
ans = sum1 + sum2 + sum3

print(ans)
