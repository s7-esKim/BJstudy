# pypy 통과 코드 pop써서 구현
N = int(input())                                # 크레인 수
cranes = list(map(int,input().split()))         # 크레인 무게
M = int(input())                                # 박스의 수
boxes = list(map(int,input().split()))          # 박스의 무게

cranes.sort(key=int, reverse=True)
boxes.sort(key=int, reverse=True)
ans = 0

if cranes[0] < boxes[0]:                       # 박스 못옮기는 경우
    ans = -1

else:
    while boxes:
        for i in cranes:
            for j in range(len(boxes)):
                if i >= boxes[j]:
                    boxes.pop(j)
                    break

print(ans)

# python 통과 코드 인덱스로 접근해서 구현
N = int(input())                                                                        # 크레인 수
cranes = list(map(int,input().split()))                                                 # 크레인 무게
M = int(input())                                                                        # 박스의 수
boxes = list(map(int,input().split()))                                                  # 박스의 무게

cranes.sort(key=int, reverse=True)
boxes.sort(key=int, reverse=True)

ans = 0
if cranes[0] < boxes[0]:                                                                # 박스 못옮기는 경우
    ans = -1

else:
    cnt = 0                                                                             # 옮긴 상자 수

    box_idx = [0] * N                                                                   # 크레인이 옮긴 박스 인덱스
    visited = [0] * M                                                                   # 상자 옮기면 1로 바꾸기

    while cnt < M:                                                                      # 다 옮길때까지 반복
        for i in range(N):
            while box_idx[i] < M:                                                       # 상자 인덱스 넘으면 종료
                if not visited[box_idx[i]] and cranes[i] >= boxes[box_idx[i]]:          # 방문하지 않고 더 큰 경우
                    visited[box_idx[i]] = 1                                             # 방문 처리
                    cnt += 1                                                            # 옮긴 상자 수 +1
                    break                                                               # while문 빠져나갈수 있도록 설정 상자를 옮겼으므로
                box_idx[i] += 1                                                         # if문을 못탄 경우 인덱스 늘려서 옮길 수 있는 상자 찾기
        ans += 1                                                                        # 반복할때마다 1씩 증가

print(ans)
