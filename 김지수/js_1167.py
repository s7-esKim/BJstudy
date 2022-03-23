import sys
sys.stdin = open('1.txt')

n = int(input())
tree = [[] for _ in range(n+1)]
visit = [0] * (n+1)
maxi = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    a = tmp[0]
    for i in range(1, len(tmp)-1, 2):
        b, c = tmp[i], tmp[i+1]
        tree[a].append((b, c))
