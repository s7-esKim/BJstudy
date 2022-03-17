# pypy3
# editor = list(input())
# s_lst = []
# T = int(input())
#
# for _ in range(T):
#     lst = input().split()
#     if lst[0] == 'L':
#         if editor:
#             s_lst.append(editor.pop())
#     elif lst[0] == 'D':
#         if s_lst:
#             editor.append(s_lst.pop())
#     elif lst[0] == 'B':
#         if editor:
#             editor.pop()
#     else:
#         editor.append(lst[1])
#
# editor = editor + s_lst[::-1]
# print(''.join(editor))
#
# python sys.stdin.readline()사용
import sys
editor = list(sys.stdin.readline().strip())
s_lst = []
T = int(sys.stdin.readline())
lst = [sys.stdin.readline().split() for i in range(T)]
for _ in range(T):
    if lst[_][0] == 'L':
        if editor:
            s_lst.append(editor.pop())
    elif lst[_][0] == 'D':
        if s_lst:
            editor.append(s_lst.pop())
    elif lst[_][0] == 'B':
        if editor:
            editor.pop()
    else:
        editor.append(lst[_][1])

editor = editor + s_lst[::-1]
print(''.join(editor))

