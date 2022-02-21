N = int(input())

len_max = 0
answer = []

for i in range(N+1):           # 두번째 수에 0부터 N까지 넣어보기
    arr = [N, i]               # 첫번째 수와 두번째 수
    j = 0
    while True:
        a = arr[j] - arr[j+1]  # 앞의 앞의 수에서 앞의 수 뺀 것 = a
        if a < 0:              # a 값이 음의 정수라면 반복문 종료
            break
        else:
            arr.append(a)      # a 값이 양의 정수라면 arr 에 추가
        j += 1                 # 그 다음 값을 구하기 위해 j에 +1

    if len(arr) > len_max:     # 최대 개수 구하기
        len_max = len(arr)
        answer = arr

print(len_max)
for i in answer:
    print(i, end=' ')
