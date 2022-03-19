from collections import deque
n, w, L = map(int,input().split()) # n:트럭수 w:다리 길이 L:최대하중
weight = list(map(int,input().split())) # [7,4,5,6] n과 길이 같음
weight = weight[::-1] # [6 5 4 7]
bridge = deque()
second = 0
for i in range(w):
    bridge.append(0)

while weight:
    second += 1  # 단위시간  += 1
    bridge.pop()  # 가장 오른쪽에 있는거는 빼
    a = weight.pop()
    if a + sum(bridge) <= L: #최대하중보다 작으면
        bridge.appendleft(a) #트럭을 다리에 올려
    else:
        weight.append(a) #다시 들어가서 기다려
        bridge.appendleft(0)

print(second+w)