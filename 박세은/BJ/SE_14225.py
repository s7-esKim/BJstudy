def dfs(i, total):
    # N번 만큼 더했으면 total 값 result 에 추가
    if i == N:
        result.add(total)
    # i번째 원소를 더하는 것과 더하지 않는 것 두 개로 나누기
    else:
        dfs(i+1, total+arr[i])
        dfs(i+1, total)


N = int(input())
arr = list(map(int, input().split()))

result = set()
dfs(0, 0)

# 0부터 시작하기 때문에 작은 값이 result 에 없다면 그 값 출력
for j in range(sum(arr)):
    if j not in result:
        print(j)
        break
# for 문이 다 끝났는데도 답이 없다면 가장 작은 값은 sum(arr)+1
else:
    print(sum(arr) + 1)
