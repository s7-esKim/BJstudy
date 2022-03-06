T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    docs = list(enumerate(lst))             # 인덱스 계산하기 편하게 튜플 형식으로 받아줌
    
    i = 0
    while i < N:                            # 반복문을 인덱스만큼 계속 돌면서
        v = docs[i]                         # v 즉, i번째 인덱의 값보다 큰게 리스트 내에 있으면
        for j in range(i+1, N):
            if v[1] < docs[j][1]:           
                docs.append(v)              # v를 리스트에 추가하고 pop으로 뽑아주고 break
                docs.pop(i)
                break
        else:                               # 만약 없다면 인덱스를 1 추가해줌
            i += 1
    
    for i in range(N):                      # 튜플 형식이므로 0 == M이면 출력
        if docs[i][0] == M:
            print(i+1)                      # 인덱스 연산이라 +1
            break

                