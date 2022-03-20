from collections import deque
def bfs():
    time = 0
    bridge = deque([0] * w)

    while t_weight:
        bridge.popleft()
        x = t_weight[0]
        if len(bridge) < w and sum(bridge) + x <= L:
            bridge.append(t_weight.popleft())
        else:
            bridge.append(0)
        time += 1
    return time + w

n, w, L = map(int, input().split())         # n : 트럭 수, w : 다리의 길이, L : 다리의 최대하중
t_weight = deque(map(int, input().split())) # 트럭의 무게

print(bfs())