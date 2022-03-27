import sys
sys.setrecursionlimit(100000)

def solution(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리
        if tree[start] < tree[i]:
            div = i
            break

    solution(start + 1, div - 1)
    solution(div, end)
    print(tree[start])

tree = []
count = 0
while count <= 10000:

    try:
        node = int(input())
    except:
        break

    tree.append(node)
    count += 1

solution(0, len(tree) - 1)