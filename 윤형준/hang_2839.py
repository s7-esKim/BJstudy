N = int(input())

cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1

else:
    print(-1)

# N이 5로 나눠지면 cnt에 그 몫을 더해서 출력
# 아니라면 N에 3을 빼고 cnt에 1 더해주고 다시 while문
# 그리고 나눠지면 cnt에 5로 나눈 몫을 더하고 출력
# 아니라면 위 반복
# 처음에는 if문 여러개로 5로 나누었을 때, 5로 나눈 나머지를 3으로 나누었을 때
# 이런식으로 진행했는데 11에서 막혀서 while문으로 바꿈