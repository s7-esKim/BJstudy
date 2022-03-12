import sys 

# 시간 초과로 인해 빠른 입출력 작성
# stack을 두개 만든 이유는 |스택1|커서|스택2| 이런식으로 풀어보려고 함

stack1 = list(sys.stdin.readline().strip())
stack2 = []
N = int(sys.stdin.readline().strip())

# 저 개념을 적용만 시키면 나머지는 문제 그대로 따라서 진행

for i in range(N):
    a = sys.stdin.readline().strip().split()
    if len(a) == 1:
        if a[0] == 'L':
            if stack1:
                stack2.append(stack1.pop())
        elif a[0] == 'D':
            if stack2:
                stack1.append(stack2.pop())
        else:
            if stack1:
                stack1.pop()
    else:
        stack1.append(a[1])

# 스택구조로 활용했기 때문에 2번째 스택은 거꾸로 출력해야 제대로 나옴!
print(''.join(stack1+stack2[::-1]))
