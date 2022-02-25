import sys
sys.stdin = open('input1.txt')

N = int(input())                       # 스위치의 개수
arr = list(map(int, input().split()))  # 스위치 상태
student = int(input())                 # 학생수
for st in range(student):
    # 학생의 성별, 받은 수
    G, s = map(int, input().split())
    s_index = s - 1
    # 학생이 남자일 때, 받은 수의 배수만 변경하기
    if G == 1:
        for i in range(s_index, N, s):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1

    # 학생이 여자일 때, 좌우 대칭을 가장 많이 포함하는 구간 변경
    if G == 2:
        start = 0
        end = 0
        i = 0
        while s_index - i >= 0 and s_index + i < N:
            # 받은 수를 중심으로 같은 값들 있으면 start 와 end 에 그 값의 index 저장
            if arr[s_index-i] == arr[s_index+i]:
                start = s_index-i
                end = s_index+i
                i += 1
            else:
                break
        # 좌우 대칭을 포함하는 구간 변경
        for j in range(start, end+1):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

for i in range(0, N, 20):
    print(*arr[i:i+20])