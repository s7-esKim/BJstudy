# 피시방 알바
# n = 손님 수 n <= 100
# list = 손님이 앉고싶어하는 자리

n = int(input()) #손님수
seat = list(map(int, input().split()))  # 앉고싶어하는자리 ex) 1,2,3

# 피시방자리 리스트
pc = [0]*101
# 거절당한사람 수
pc_refused = 0

for i in seat: # 앉고싶어하는 자리 수 만큼 순회(즉 손님수)
    if pc[i] != 0: # 만약 pc리스트의 i번째(첫번째 원하는 자리) 0이 아니라면 거절
        pc_refused += 1
    else: # 0이라면 원하는 자리가 있다면 pc의 i번째(원하는자리) 에 +1
        pc[i] += 1

print(pc_refused)