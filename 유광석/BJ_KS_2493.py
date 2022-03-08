T = int(input())

top = list(map(int, input().split()))   # top 높이를 리스트로 받아준다.
cnt = [0] * T                           # 결과를 저장할 cnt 배열
stack = []                              # 송신을 못한 탑들을 담아둘 stack

for i in range(T):                      # top의 갯수만큼 순회를 돈다.
    while stack:                        # 만약 스택이 있으면 (= 레이저 신호를 받지 못한 탑이 있으면)
        if stack[-1][1] > top[i]:       # stack[-1] 뒤에서부터 확인하면서 현재 탑의 높이와 비교해서
            cnt[i] = stack[-1][0] + 1   # 신호를 받을 수 있는 탑이면 cnt 배열에 index값에 1을 더해서 추가해준다.
            break
        else:
            stack.pop()                 
    stack.append((i, top[i]))           # 인덱스 연산이 귀찮아서 그냥 튜플로 인덱스와 묶어서 넣어줌

print(*cnt)                             # 결과 언팩해서 출력
