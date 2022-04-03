import sys
input = sys.stdin.readline

# 내림차순 정렬 : 무거운 물건
N = int(input())
crane = list(map(int, input().split()))
crane = sorted(crane, reverse=True)
M = int(input())
box = list(map(int, input().split()))
box = sorted(box, reverse=True)

# 옮길 수 없는 박스가 있다면 -1 출력
if box[0] > crane[0]:
    print(-1)
else:
    time = 0   # 시간
    count = 0  # while 문을 종료하기 위해
    visited = [0] * M    # 박스를 옮겼는지 확인할 list
    crane_box = [0] * N  # 방금 옮긴 박스 번호를 저장할 list
    # 박스를 옮길 때 마다 count += 1, count == M 이 되면 박스를 다 옮긴 것
    while count < M:
        time += 1
        for i in range(N):
            # 찾아볼 박스 번호가 박스의 개수 보다 많으면 종료
            # crane_box[i] -> 우리가 옮길 박스의 index
            while crane_box[i] < M:
                # crane 무게가 박스의 무게보다 크고 그 박스가 아직 옮겨지지 않은 박스라면
                if crane[i] >= box[crane_box[i]] and visited[crane_box[i]] == 0:
                    # 옮긴 박스로 처리, 박스의 index 번호 증가, count += 1
                    visited[crane_box[i]] = 1
                    crane_box[i] += 1
                    count += 1
                    break
                # 박스를 옮기지 않았지만 다음 박스는 옮길 수 있는 지 확인 하기 위해 박스 번호 += 1
                crane_box[i] += 1
    print(time)
