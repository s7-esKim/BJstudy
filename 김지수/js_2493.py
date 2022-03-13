import sys
sys.stdin = open('1.txt')

n = int(input()) #탑의 갯수
top = list(map(int, input().split()))
ans = [0] * n
stack = []
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])
print(*ans)






# answer = [0] * len(top_lst)
# stack = []
# for i in range(len(top_lst)-1, -1, -1):
#     while stack and top_lst[stack[-1]] < top_lst[i] :
#         answer[stack.pop()] = i+1
#     stack.append(i)
#
# print(*answer)



# stack = [] # 수신 가능한 탑
# result = [0] * n
# for i in range(n): # 6 9 5 7 4
#     top = top_lst[i]
#     while stack and top_lst[stack[-1]] < top: # i번째 탑보다 낮은 타워는 i+1번째 이상에서 의미 x
#         stack.pop() # 빼버리기
#     if stack:
#         result[i] = stack[-1] + 1
#     stack.append(i)
# print(' '.join(map(str, result)))
