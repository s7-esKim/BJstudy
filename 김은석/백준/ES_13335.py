n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0
truck_weight = 0

while bridge:
    time += 1
    truck_weight -= bridge.pop(0)
    if trucks:
        if truck_weight + trucks[0] <= L:
            bridge.append(trucks[0])
            truck_weight += trucks[0]
            trucks.pop(0)
        else:
            bridge.append(0)

print(time)