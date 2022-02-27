W, H = map(int, input().split()) # 가로 세로 길이
N = int(input()) # 잘라야하는 점선의 개수

w_li = [0,H]
h_li = [0,W]

for i in range(N):
    A, B = map(int, input().split())
    if A == 0:
        w_li.append(B)
    else:
        h_li.append(B)

w_li.sort()
h_li.sort()

paper1 = []
paper2 = []
for i in range(len(w_li)-1):
    paper1.append(w_li[i+1]-w_li[i])

for j in range(len(h_li)-1):
    paper2.append((h_li[j+1]-h_li[j]))

print(max(paper1) * max(paper2))