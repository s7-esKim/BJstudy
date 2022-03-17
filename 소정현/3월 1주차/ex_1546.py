n = int(input())

k = list(map(int, input().split()))

def new_score(score, max_score):
    newest_score = (score/max_score)*100
    return newest_score
max_score = max(k)

for i in range(n):
    k[i] = new_score(k[i], max_score)

print(sum(k)/n)