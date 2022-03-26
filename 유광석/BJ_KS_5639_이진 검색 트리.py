import sys
sys.setrecursionlimit(20000)


# def change(n, r):
#     if n > r:
#         if tree[r][1] == 0:
#             tree[r][1] = n
#         else:
#             r = tree[r][1]
#             change(n, r)
#     else:
#         if tree[r][0] == 0:
#             tree[r][0] = n
#         else:
#             r = tree[r][0]
#             change(n, r)

# def post(r):
#     if r:
#         post(tree[r][0])
#         if tree[r][1] != 0:
#             print(tree[r][1])
#         print(r)


# root = int(input())
# tree = [[0, 0] for _ in range(10**6+1)]

def post(s, e):
    if s > e:
        return
    
    root = nums[s]
    i = s + 1

    while i <= e:
        if nums[i] > root:
            break
        i += 1
    
    post(s + 1, i - 1)
    post(i, e)
    print(root)


nums = []
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break
post(0, len(nums) - 1)


