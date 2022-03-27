lst1 = []   # 전위순회 리스트
lst2 = []   # 중위순회 리스트
lst3 = []   # 후위순회 리스트
# 전위순회
def front_order(v):
    if v:
        lst1.append(tree[v])
        front_order(ch1[v])
        front_order(ch2[v])

# 중위순회
def in_order(v):
    if v:
        in_order(ch1[v])
        lst2.append(tree[v])
        in_order(ch2[v])

# 후위순회
def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        lst3.append(tree[v])

tree = [0] * 27 # node 리스트
ch1 = [0] * 27  # 왼쪽 자식  리스트
ch2 = [0] * 27  # 오른쪽 자식 리스트

N = int(input())
lst = [0]
for i in range(1, N+1):
    lst.append(input().split())

for j in range(1, N+1):
    if lst[j][0] != '.':
        tree[ord(lst[j][0])-64] = lst[j][0]
    if lst[j][1] != '.':
        ch1[ord(lst[j][0])-64] = (ord(lst[j][1])-64)
    if lst[j][2] != '.':
        ch2[ord(lst[j][0])-64] = (ord(lst[j][2])-64)

front_order(1)
in_order(1)
post_order(1)
print("".join(lst1))
print("".join(lst2))
print("".join(lst3))