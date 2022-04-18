from collections import deque

def bfs(idx):
    cnt = 1     # 컴퓨터 갯수
    q = deque()
    q.append(idx)
    v = [0 for _ in range(N + 1)]   # 방문 리스트 생성
    v[idx] = 1
    while q:
        ni = q.popleft()
        for i in hak[ni]:
            if not v[i]:
                v[i] = 1
                q.append(i)
                cnt += 1
    return cnt


N, M = map(int, input().split())
hak = [[] for _ in range(N + 1)]
# 접근을 편하게 하기 위해 M만큼 for문을 돌면서 해킹 리스트에 추가
for i in range(M):
    a, b = map(int, input().split())
    hak[b].append(a)

result = []     # 컴퓨터 번호와 갯수를 담을 리스트
max_cnt = 0     # 갯수의 최대값
for si in range(1, N + 1):
    if hak[si]:             # 신뢰하는 컴퓨터가 있을 때
        cnt = bfs(si)
        if max_cnt <= cnt:  # 최대값 갱신
            max_cnt = cnt
        result.append([si, cnt])    # 컴퓨터 번호와 갯수 추가

for i, cnt in result:
    # 컴퓨터가 최대 갯수이면 출력
    if max_cnt == cnt:
        print(i, end=' ')