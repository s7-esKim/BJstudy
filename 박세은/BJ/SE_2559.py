# 시간 초과 해결 방법
# 불필요한 덧셈을 줄이기
# 더한 값(sum(arr([:K])에서 처음 값을 빼고 다음에 올 값을 더하기

# 전체 날짜 수, 연속적인 날짜 수
N, K = map(int, input().split())
arr = list(map(int, input().split()))

temp = [sum(arr[:K])]

for i in range(N-K):
    temp.append(temp[i] - arr[i] + arr[i+K])

print(max(temp))

