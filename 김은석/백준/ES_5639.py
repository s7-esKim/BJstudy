def postorder(start, end):
    if start > end:
        return

    divide = end + 1  # 나눌위치
    for i in range(start + 1, end + 1):
        if post_list[start] < post_list[i]:
            divide = i
            break

    postorder(start + 1, divide - 1)
    postorder(divide, end)
    print(post_list[start])


import sys
sys.setrecursionlimit(10 ** 9)

post_list = []
cnt = 0
while cnt <= 10000:
    try:
        preorder = int(input())
    except:
        break
    post_list.append(preorder)
    cnt += 1

postorder(0, len(post_list) - 1)