import sys
sys.stdin = open('input.txt')

N = int(input())  # 정수의 개수
stack = []        # 숫자를 쌓아줄 stack
arr = []          # 원하는 수열
answer = []       # push -> +, pop -> -
n = 1

for i in range(N):
    a = int(input())

    # a 까지의 값을 stack 에 넣기
    while n <= a:
        stack.append(n)
        answer.append('+')
        n += 1

    # stack 의 top 과 a 의 값이 같으면 제거
    if stack[-1] == a:
        arr.append(stack.pop())
        answer.append('-')
    # 값을 꺼낼 수가 없으면 arr 을 비우고 for 문 종료
    else:
        arr = []
        break

# arr 에 값이 있으면 가능
if arr:
    print('\n'.join(answer))
# arr 에 값이 없으면 불가능
else:
    print('NO')







