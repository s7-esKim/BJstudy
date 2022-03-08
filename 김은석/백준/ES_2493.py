N = int(input())
top = list(map(int, input().split()))
# 69574 왼쪽으로 신호 발사
# 1. 맨 처음은 무조건 0 을 출력한다.
# 2. 두번째부터는 앞에 인덱스의 숫자가 큰 경우에 신호를 받을 수 있다.
# 3. 스택 문제인데 스택으로 안풀어도 해결 가능 할듯?? 그래도 스택 관련으로 풀어보기
# 4. 출력의 결과는 신호를 받는 인덱스 번호를 출력한다. 즉 탑의 순서를 출력한다 0 0 2 2 4
stack = [[1, top[0]]] # 앞은 타워번호 뒤는 타워높이
result = [0] # 결과값

for i in range(1, N):
    while stack:
        if stack[-1][1] > top[i]: # 6이 9보다 작으니까 result에는 0이 들어가야함, 9는 5보다 크니까 result에는 2가 들어가야함
            result.append(stack[-1][0])
            stack.append([i+1, top[i]])
            break
        else:
            stack.pop()

    if not stack:
        result.append(0)
        stack.append([i+1, top[i]])

print(*result)