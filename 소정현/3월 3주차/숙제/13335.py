'''
입력 데이터는 표준입력을 사용한다. 입력은 두 줄로 이루어진다.
입력의 첫 번째 줄에는 세 개의 정수
n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)이 주어지는데,
n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다.
입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데,
ai는 i번째 트럭의 무게를 나타낸다.
4 2 10
7 4 5 6
'''
from collections import deque

n, w, L = map(int, input().split())

dari_queue = deque()
for _ in range(w):
    dari_queue.append(0)

truck_queue = deque(map(int,input().split()))


day = 0
dari_weight = 0
while truck_queue:
    day += 1
    bye = dari_queue.popleft()
    dari_weight -= bye
    if dari_weight + truck_queue[0] <= L:
        truck = truck_queue.popleft()
        dari_weight += truck
        dari_queue.append(truck)
    else:
        dari_queue.append(0)

print(day + w)