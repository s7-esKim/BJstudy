def solution(num, idx, p, m, mul, div):
    global max_value, min_value
    if idx == N:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return

    if p > 0:
        solution(num + number[idx], idx + 1, p - 1, m, mul, div)
    if m > 0:
        solution(num - number[idx], idx + 1, p, m - 1, mul, div)
    if mul > 0:
        solution(num * number[idx], idx + 1, p, m, mul - 1, div)
    if div > 0:
        solution(int(num / number[idx]), idx + 1, p, m, mul, div - 1)


N = int(input())
number = list(map(int,input().split())) # 숫자
plus, minus, multi, divide = map(int, input().split()) # 덧셈 뺄셈 곱셈 나눗셈

max_value = -99999999999999999
min_value = 99999999999999999

solution(number[0], 1, plus, minus, multi, divide)
print(max_value)
print(min_value)