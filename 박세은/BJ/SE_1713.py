import sys
input = sys.stdin.readline

N = int(input())
R = int(input())
arr = list(map(int, input().split()))

answer = []
score = []
for i in arr:
    if i in answer:
        for j in range(len(answer)):
            if i == answer[j]:
                score[j] += 1
    else:
        if len(answer) >= N:
            for j in range(N):
                if score[j] == min(score):
                    del answer[j]
                    del score[j]
                    break
        answer.append(i)
        score.append(1)

answer.sort()
print(*answer)
