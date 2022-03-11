N = int(input())  # 탑의 개수
arr = list(map(int, input().split()))  # 탑의 번호
stack = []
answer = []

# 원소의 개수 만큼 반복
for i in range(N):
    # stack 이 차있으면 stack 의 마지막 탑의 높이와 i 번째의 높이 비교
    # stack 에 있는 탑의 높이가 더 크다면 거기서 신호를 출력
    # 만약 stack 에 있는 탑의 높이가 더 크지 않다면 그 탑은 신호 출력 X -> 비교대상 제외
    while stack:
        if stack[-1][1] > arr[i]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    # stack 이 비어있다면 비교할 대상이 없는 것 = 수신 X
    if len(stack) == 0:
        answer.append(0)
    # 비교가 끝나면 그 탑의 index 번호와 탑의 높이를 stack 에 쌓기
    stack.append([i, arr[i]])

print(' '.join(map(str, answer)))
