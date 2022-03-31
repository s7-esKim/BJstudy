N = int(input())    # 크레인 개수
crane = list(map(int, input().split())) # 크레인 리스트
M = int(input())    # 박스 개수
box = list(map(int, input().split()))   # 박스 리스트

# 제일 큰 것부터 정렬
crane.sort(reverse=True)
box.sort(reverse=True)

v = [0] * N # 박스를 옮긴 횟수
while len(box) >= 1:
    # 박스를 옮길 수 없으므로 종료
    if crane[0] < box[0]:
        print('-1')
        exit()

    for i in range(len(crane)):     
        for j in range(len(box)):
            if crane[i] >= box[j]:  # 크레인이 박스를 옮길 수 있는지 판단
                v[i] += 1   # 횟수 체크
                box.pop(j)  # 박스 리스트 하나 제거
                break       

print(max(v))   # 박스를 옮긴 횟수 중 제일 큰 값 출력