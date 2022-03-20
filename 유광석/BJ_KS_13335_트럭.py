from collections import deque

# N : 트럭수, W : 다리의 길이, L : 다리의 하중
N, W, L = map(int, input().split())
trucks = deque(map(int, input().split()))
onbridge = deque([0]*W)
time = 0


while onbridge:                                # 다리에 truck이 없을 때 까지
    time += 1                                  # time 은 순회 1번당 1씩 증가                             
    onbridge.popleft()                         # 다리의 맨 왼쪽을 뽑아서 버림
    if trucks:                                 # 만약에 다리를 지나야할 트럭이 남아있고
        if sum(onbridge) + trucks[0] <= L:     # 다리의 하중이 견딜 수 있으면
            onbridge.append(trucks.popleft())  # 트럭의 맨 왼쪽을 뽑아서 다리에 추가해줌
        else:
            onbridge.append(0)                 # 만약 견딜 수 없으면 0을 추가

print(time)
        

