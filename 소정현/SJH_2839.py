# n = int(input())
# tot = 0
# min_tot = float('inf')
# i = 0
# while True:
#     n -= 5
#     i += 1
#     if n<0:
#         print(-1)
#         break
#     if n % 5 == 0:
#         tot = n//5
#         print(tot + i)
#         break
#     else:
#         if n % 3 == 0:
#             tot = n/3 + i
#             print(tot)
#             if tot < min_tot:
#                 min_tot = tot
#         else:
#             pass
    
#     if n == 3:
#         print(int(min_tot))
#         break
        
n = int(input())
min_tot = float('inf')
for i in range(n//5 + 1):
    if n % 3 == 0:
        tot = n//3 + i
        if min_tot > tot:
            min_tot = tot
    n -= 5
    if n % 5 == 0:
        min_tot = n//5 + i + 1
    

if min_tot == float('inf'):
    print(-1)
else:
    print(min_tot)
