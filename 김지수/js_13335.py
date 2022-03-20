import sys
from _collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

answer = 0
bridge = deque([0 for _ in range(W)])

while trucks:
    bridge.popleft()
    if len(bridge) < W:
        if sum(bridge) + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
    answer += 1
answer += W
print(answer)