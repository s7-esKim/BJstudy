from collections import deque

N, K = map(int, input().split())
sam = list(map(int, input().split()))
visited = set()     # 처음엔 리스트로 받았는데 시간 초과로 인해서 set()으로 받음

q = deque()
for i in sam:
    q.append((i, 1))    # 샘터의 위치, 거리 추가
    visited.add(i)

result = 0  # 결과
# cnt = 0
while q:
    # 종료 조건
    if K <= 0:
        break
    si, length = q.popleft()
    for h in [1,-1]:
        ni = si+h
        if ni not in visited and K > 0: # 방문 하지 않았고 K가 0보다 크면
            visited.add(ni)
            result += length
            K -= 1
            # cnt += 1
            q.append((ni, length+1))

print(result)