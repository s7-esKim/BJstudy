import sys
input = sys.stdin.readline
root = int(input())

min_arr = []
max_arr = []

while True:
    try:
        node = int(input())
    except:
        break
    if node < root:
        min_arr.append(node)
    else:
        max_arr.append(node)


tree_arr = [root]


print(min_arr)
print(max_arr)