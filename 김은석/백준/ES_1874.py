N = int(input()) # 1 ~ n 까지의 수를 스택
stack = [] # 내가 스택으로 쓸 임시 리스트
result = [] # + -로 쓸 값들 push + pop -
# 4 3 6 8 7 5 2 1 << + + + + - - + + - + - - - - -
# 1 2 5 3 4 << No : 오름차순으로 push해야하는데 4보다 3을 먼저 pop할수가 없음
cnt = 1
flag = True
for _ in range(N):
    number = int(input())
    # 중복되면 안되게 해야 함
    # for i in range(number):
    #     stack.append(i)
    #     result.append('+')
    while number >= cnt:
        stack.append(cnt)
        cnt += 1
        result.append('+')

    if stack[-1] == number:
        stack.pop()
        result.append('-')

    else:
        flag = False

if flag:
    for i in result:
        print(i)
else:
    print('NO')

