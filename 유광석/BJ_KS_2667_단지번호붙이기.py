from pprint import pprint

# 1인 좌표값을 받아서 사방으로 인접한 부분의 1에 num을 더해줌
def check(a, b, arr):
    da = [-1, 1, 0, 0]
    db = [0, 0, -1, 1]
    
    for i in range(4):
        na = a + da[i]
        nb = b + db[i]
        
        if 0 <= na < N and 0 <= nb < N and arr[na][nb] == 1:
            arr[na][nb] += num
            check(na,nb,arr) 
    else:
        return

# 좌표값이 1인 점을 찾고 위의 check 함수를 실행함
# 만약에 1인 점이 없으면 flag를 True로 바꿔주고 종료
def find(arr):
    global flag
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                arr[i][j] += num
                check(i, j, arr)
                return arr
    else:
        flag = True
        return arr

# 인풋값과 단지 구별을 위한 num 설정
N = int(input())
arr = [list(map(int,  input())) for _ in range(N)]
num = 0
flag = False

# 좌표값이 1이 없을 때 까지 (= 1이면 아직 방문하지 않은 곳)
while True:
    num += 1
    find(arr)
    if flag:
        break

# +1 부터 단지수를 계산했으므로 -1로 출력하고
print(num - 1)

# 2부터 총 단지 수 만큼 순회를 돌면서 cnt리스트에 값을 추가함
cnt = []
for i in range(2, num):
    c = 0
    for j in range(N):
        for k in range(N):
            if arr[j][k] == i:
                c += 1
    if c == 0:
        break
    cnt += [c]

# 출력 형식에 맞게 정렬 후 출력!
cnt.sort()

for i in cnt:
    print(i)
