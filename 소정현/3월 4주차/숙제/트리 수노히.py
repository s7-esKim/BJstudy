'''
8
A B C
B D .
C E F
E . .
F . G
D . .
G . Z
Z . .
'''
import sys

input = sys.stdin.readline

N = int(input())

# connect_lst = [[] for _ in range(N)]
connect_lst = [[] for _ in range(N)]
alphabet_dict = {}
# for i in range(26):
#     alphabet_dict[chr(i+65)] = i
#     connect_lst.append([])
# print(alphabet_dict)
# alphabet_dict = {'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}

for _ in range(N):
    i, j, k = input().split()
    alphabet_dict[i] = _
    connect_lst[alphabet_dict[i]].append(j)
    connect_lst[alphabet_dict[i]].append(k)

def pre_order(T):
    if T != '.':
        print(T, end = '')
        pre_order(connect_lst[alphabet_dict[T]][0])
        pre_order(connect_lst[alphabet_dict[T]][1])


def post_order(T):
    if T != '.':
        post_order(connect_lst[alphabet_dict[T]][0])
        print(T, end='')
        post_order(connect_lst[alphabet_dict[T]][1])


def in_order(T):
    if T != '.':
        in_order(connect_lst[alphabet_dict[T]][0])
        in_order(connect_lst[alphabet_dict[T]][1])
        print(T, end='')

pre_order('A')
print()
post_order('A')
print()
in_order('A')
