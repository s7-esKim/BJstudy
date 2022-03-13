K = int(input())        # K 입력
lst = []                # 빈 리스트 생성
for i in range(K):      # K개의 줄만큼 순회
    num = int(input())  # 숫자 입력
    if num == 0:        # 만약 숫자가 0이면 lst에 마지막 숫자 빼냄
        lst.pop()
    else:               # 아니면 리스트에 추가
        lst.append(num)
print(sum(lst))         # lst 안의 최종합 출력
