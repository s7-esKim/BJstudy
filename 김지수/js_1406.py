import sys
from collections import deque
 
s1 = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
 
s2 = deque()
 
for i in range(n):
    order = sys.stdin.readline().strip().split()
    if order[0] == "P":
        s1.append(order[1])     
    elif order[0] == "L":
        if len(s1) == 0:
            continue
        else:
            s2.appendleft(s1.pop())   
    elif order[0] == "D":
        if len(s2) == 0:
            continue
        else:
            s1.append(s2.popleft())
    elif order[0] == "B":
        if len(s1) == 0:
            continue
        else:
            s1.pop()
 
print(''.join(s1) + ''.join(list(s2)))