def dfs(num, par):
    par[num] = -2
    # par을 돌면서 삭제 노드의 손자들이 있다면 그 노드들도 -2로 바꿈
    for i in range(len(par)):
        if num == par[i]:
            dfs(i, par)

N = int(input())                        # 노드 갯수
par = list(map(int, input().split()))   # 각 인덱스에 부모노드가 저장된 리스트
d = int(input())                        # 삭제 노드

dfs(d, par)

cnt = 0
# 자식이 없는 리프노드를 찾는 for문
for i in range(len(par)):
    if par[i] != -2 and i not in par:   # 삭제되었지 않고, 노드번호가 par에 포함되어 있지 않으면(자식이 없으면)
        cnt += 1
print(cnt)
