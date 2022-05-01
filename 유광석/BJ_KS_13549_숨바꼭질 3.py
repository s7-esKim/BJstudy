from collections import deque

def BFS(s):
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()

        if v == K:
            print(lst[v])
            exit()

        for i in (v*2, v-1, v+1):
            if 0 <= i < 100001 and lst[i] == -1:
                if i == v*2:
                    lst[i] = lst[v]
                    q.appendleft(i)
                else:
                    lst[i] = lst[v] + 1
                    q.append(i)

                
            

N, K = map(int, input().split())
lst = [-1] * 100001
lst[N] = 0
BFS(N)